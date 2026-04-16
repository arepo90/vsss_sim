import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from sim_msgs.msg import FieldData, LowCmd, HighCmd, ObjData, Settings
from sim_msgs.srv import Controller
from enum import IntEnum
import threading
import math
import time

# strat2: drop-in replacement for strat. Same topic/service interface.
# Additions over strat: open-post aiming when a blocker is in the shot
# corridor, per-role ball-lookahead tunables, kept per-feedback empty
# tactical obstacle list (enemies are NOT auto-populated as obstacles).


class State(IntEnum):
    HALT = -1
    PAUSE = 0
    PLAY = 1


FIELD_LENGTH = 17
FIELD_HEIGHT = 13
GOAL_WIDTH = 3
TEAM_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
OP_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
DEF_POS = np.array([(FIELD_LENGTH - 4) / 2, 0.0])
MID_POS = [np.array([0, 3]), np.array([0, -3]), np.array([0, 0])]
FIELD_LIMS = np.array([8, 6])

ATTRACTIVE_GAIN = 0.5
REPULSIVE_GAIN = 2
REPULSION_RADIUS = 1
GOAL_TOLERANCE = 1
TANGENTIAL_GAIN = 3
TARGET_OFFSET = 0.5
COLINEARITY = 0.975
STRIKE_APPROACH_DIST = 2.0
ATTACKER_SWAP_MARGIN = 0.3
ATTACKER_SWAP_DWELL = 0.5

USE_LOCAL = True

BALL_FRICTION = 3.0
ATTACKER_LOOKAHEAD_MIN_DIST = 2.0
CORRIDOR_WIDTH = 0.6
AIM_AT_OPEN_POST = True
POST_MARGIN = 0.4
BLOCKER_BALL_EXCLUSION = 1.2


def _unit(v):
    n = np.linalg.norm(v)
    if n < 1e-9:
        return np.array([0.0, 0.0])
    return v / n


def in_corridor(ball_pos: np.ndarray, target_pos: np.ndarray, obstacle_pos: np.ndarray, width: float) -> bool:
    shot_dir = target_pos - ball_pos
    length = np.linalg.norm(shot_dir)
    if length < 1e-6:
        return False
    shot_dir = shot_dir / length
    perp = np.array([-shot_dir[1], shot_dir[0]])
    rel = obstacle_pos - ball_pos
    along = float(np.dot(rel, shot_dir))
    if along < BLOCKER_BALL_EXCLUSION or along > length:
        return False
    lateral = abs(float(np.dot(rel, perp)))
    return lateral <= width


def blocker_in_shot(ball_pos: np.ndarray, target_pos: np.ndarray, enemies: list, width: float):
    best = None
    best_along = float('inf')
    shot_dir_vec = target_pos - ball_pos
    length = np.linalg.norm(shot_dir_vec)
    if length < 1e-6:
        return None
    shot_dir = shot_dir_vec / length
    perp = np.array([-shot_dir[1], shot_dir[0]])
    for e in enemies:
        rel = e - ball_pos
        along = float(np.dot(rel, shot_dir))
        if along < BLOCKER_BALL_EXCLUSION or along > length:
            continue
        lateral = abs(float(np.dot(rel, perp)))
        if lateral > width:
            continue
        if along < best_along:
            best_along = along
            best = e
    return best


def pick_aim_point(ball_pos: np.ndarray, goal_pos: np.ndarray, goal_width: float, enemies: list) -> np.ndarray:
    if not AIM_AT_OPEN_POST:
        return goal_pos
    post_a = np.array([goal_pos[0], +goal_width / 2 - POST_MARGIN])
    post_b = np.array([goal_pos[0], -goal_width / 2 + POST_MARGIN])
    blocker_center = blocker_in_shot(ball_pos, goal_pos, enemies, CORRIDOR_WIDTH)
    if blocker_center is None:
        return goal_pos
    blocker_a = blocker_in_shot(ball_pos, post_a, enemies, CORRIDOR_WIDTH * 0.75)
    blocker_b = blocker_in_shot(ball_pos, post_b, enemies, CORRIDOR_WIDTH * 0.75)
    if blocker_a is None and blocker_b is None:
        if blocker_center[1] >= 0:
            return post_b
        return post_a
    if blocker_a is None:
        return post_a
    if blocker_b is None:
        return post_b
    return goal_pos


class SkillLib:
    def moveToPointOrg(self, robot, target_pos, target_theta, obstacles, bypass=False):
        robot_pos = np.array([robot.x, robot.y])
        robot_vel = np.array([robot.vx, robot.vy])
        target_pos = np.clip(target_pos, -FIELD_LIMS, FIELD_LIMS)
        net_vector = self._calculate_potential_field_vector_org(robot_pos, robot_vel, target_pos, obstacles, bypass)
        if USE_LOCAL:
            vx_robot, vy_robot = self._world_to_robot_frame(net_vector, robot.theta)
        else:
            vx_robot, vy_robot = net_vector
        vx_capped, vy_capped = self._cap_speed(vx_robot, vy_robot)
        cmd = LowCmd()
        cmd.robot_id = robot.obj_id
        cmd.vx = vx_capped
        cmd.vy = vy_capped
        cmd.dtheta = (target_theta - robot.theta + 180) % 360 - 180
        return cmd, target_pos

    def moveToStrikeOrg(self, robot, target_pos, target_theta, obstacles, strike_dir):
        robot_pos = np.array([robot.x, robot.y])
        vec_robot_to_target = target_pos - robot_pos
        dist_to_target = np.linalg.norm(vec_robot_to_target)
        if dist_to_target < 1e-6:
            alignment = 1.0
        else:
            norm_vec_robot_to_target = vec_robot_to_target / dist_to_target
            alignment = np.dot(norm_vec_robot_to_target, strike_dir)
        if alignment > COLINEARITY:
            return self.moveToPointOrg(robot, target_pos + strike_dir * TARGET_OFFSET, target_theta, [])
        return self.moveToPointOrg(robot, target_pos - strike_dir * TARGET_OFFSET, target_theta, obstacles + [target_pos], True)

    def moveToPoint(self, robot, target_pos, target_theta, obstacles, bypass=False, ball_obstacle=None):
        robot_pos = np.array([robot.x, robot.y])
        robot_vel = np.array([robot.vx, robot.vy])
        target_pos = np.clip(target_pos, -FIELD_LIMS, FIELD_LIMS)
        V_MAX = 1.0
        A_0 = 0.01
        gradient_vector = self._calculate_potential_field_vector(robot_pos, robot_vel, target_pos, obstacles, bypass, ball_obstacle)
        distance_to_goal = np.linalg.norm(target_pos - robot_pos)
        if np.linalg.norm(gradient_vector) < 1e-6 or distance_to_goal < 1e-6:
            net_vector = np.array([0., 0.])
        else:
            direction = gradient_vector / np.linalg.norm(gradient_vector)
            desired_speed = min(V_MAX, (2 * A_0 * distance_to_goal) ** 0.5)
            net_vector = direction * desired_speed
        if USE_LOCAL:
            vx_robot, vy_robot = self._world_to_robot_frame(net_vector, robot.theta)
        else:
            vx_robot, vy_robot = net_vector
        vx_capped, vy_capped = self._cap_speed(vx_robot, vy_robot)
        cmd = LowCmd()
        cmd.robot_id = robot.obj_id
        cmd.vx = vx_capped
        cmd.vy = vy_capped
        cmd.dtheta = (target_theta - robot.theta + 180) % 360 - 180
        return cmd, target_pos

    def moveToStrike(self, robot, target_pos, target_theta, obstacles, strike_dir):
        robot_pos = np.array([robot.x, robot.y])
        vec_robot_to_target = target_pos - robot_pos
        dist_to_target = np.linalg.norm(vec_robot_to_target)
        if dist_to_target > STRIKE_APPROACH_DIST:
            return self.moveToPoint(robot, target_pos + strike_dir * TARGET_OFFSET, target_theta, obstacles)
        if dist_to_target < 1e-6:
            alignment = 1.0
        else:
            norm_vec_robot_to_target = vec_robot_to_target / dist_to_target
            alignment = np.dot(norm_vec_robot_to_target, strike_dir)
        transition_start = 0.8
        transition_width = COLINEARITY - transition_start
        mu = np.clip((COLINEARITY - alignment) / transition_width, 0.0, 1.0)
        target_aligned = target_pos + strike_dir * TARGET_OFFSET
        target_misaligned = target_pos - strike_dir * TARGET_OFFSET
        final_target = (mu * target_misaligned) + ((1.0 - mu) * target_aligned)
        ball_obstacle_param = (target_pos, mu)
        return self.moveToPoint(robot, final_target, target_theta, obstacles, ball_obstacle=ball_obstacle_param)

    def _calculate_potential_field_vector_org(self, robot_pos, robot_vel, target_pos, obstacles, bypass=False):
        direction = target_pos - robot_pos
        distance = np.linalg.norm(direction)
        if distance < 1e-6:
            return np.array([0., 0.])
        direction /= distance
        v_max = ATTRACTIVE_GAIN
        d0 = GOAL_TOLERANCE
        n = 2
        mag = v_max * (distance ** n) / (distance ** n + d0 ** n + 1e-9)
        attractive_vector = direction * mag
        net_repulsive_vector = np.array([0.0, 0.0])
        for obs in obstacles:
            net_repulsive_vector += self._obstacle_force(robot_pos, target_pos, obs, radial=not bypass, scale=1.0)
        return attractive_vector + net_repulsive_vector

    def _obstacle_force(self, robot_pos, target_pos, obstacle_pos, radial=True, scale=1.0):
        vec_from_obs = robot_pos - obstacle_pos
        dist = np.linalg.norm(vec_from_obs)
        if dist >= REPULSION_RADIUS or dist < 1e-6 or scale <= 0:
            return np.array([0.0, 0.0])
        radial_dir = vec_from_obs / dist
        repulsion_magnitude = REPULSIVE_GAIN * (1.0 / dist - 1.0 / REPULSION_RADIUS)
        radial_force = repulsion_magnitude * radial_dir if radial else np.array([0.0, 0.0])
        perp_a = np.array([-radial_dir[1], radial_dir[0]])
        perp_b = -perp_a
        goal_dir = target_pos - robot_pos
        goal_norm = np.linalg.norm(goal_dir)
        if goal_norm > 1e-6:
            goal_dir = goal_dir / goal_norm
            tangential_dir = perp_a if np.dot(perp_a, goal_dir) >= np.dot(perp_b, goal_dir) else perp_b
        else:
            tangential_dir = perp_a
        tangential_force = TANGENTIAL_GAIN * repulsion_magnitude * tangential_dir
        return (radial_force + tangential_force) * scale

    def _calculate_potential_field_vector(self, robot_pos, robot_vel, target_pos, obstacles, bypass=False, ball_obstacle=None):
        direction = target_pos - robot_pos
        distance = np.linalg.norm(direction)
        if distance < 1e-6:
            attractive_vector = np.array([0., 0.])
        else:
            attractive_vector = direction / distance
        net_repulsive_vector = np.array([0.0, 0.0])
        for obs in obstacles:
            net_repulsive_vector += self._obstacle_force(robot_pos, target_pos, obs, radial=True, scale=1.0)
        if ball_obstacle is not None:
            ball_pos, repulsion_scale = ball_obstacle
            net_repulsive_vector += self._obstacle_force(robot_pos, target_pos, ball_pos, radial=False, scale=repulsion_scale)
        return attractive_vector + net_repulsive_vector

    def _world_to_robot_frame(self, vector, robot_theta_deg):
        theta_rad = np.deg2rad(-robot_theta_deg)
        c, s = np.cos(theta_rad), np.sin(theta_rad)
        vx_world, vy_world = vector[0], vector[1]
        vx_robot = c * vx_world + s * vy_world
        vy_robot = -s * vx_world + c * vy_world
        return vx_robot, vy_robot

    def _cap_speed(self, vx, vy):
        speed = np.sqrt(vx ** 2 + vy ** 2)
        if speed > 1:
            return vx / speed, vy / speed
        return vx, vy


class Strat(Node):
    def __init__(self):
        super().__init__('strat2')
        self.skills = SkillLib()

        self.field_subscriber = self.create_subscription(FieldData, 'field_data', self.gpCB, 10)
        self.settings_subscriber = self.create_subscription(Settings, 'settings', self.settingsCB, 10)
        self.active_subscriber = self.create_subscription(Int32MultiArray, 'active', self.activeCB, 10)
        self.controller_service = self.create_service(Controller, 'strat/controller', self.controllerCB)

        self.cmd_publishers = {i: self.create_publisher(LowCmd, f'/low{i}', 10) for i in range(3)}
        self.tgt_publishers = {i: self.create_publisher(HighCmd, f'/high{i}', 10) for i in range(3)}

        self.get_logger().info("Strategist2 node initialized.")
        self.cmds = [None, None, None]
        self.tgts = [None, None, None]
        self.timer = self.create_timer(0.1, self.send)

        self.state = 0
        self.mod = 0
        self.params = [HighCmd, HighCmd, HighCmd]
        self.mapping = [-1, -1, -1]
        self.active = [0, 0, 0]
        self.mutex = threading.Lock()
        self.current_attacker = -1
        self.attacker_challenger = -1
        self.challenger_since = 0.0

    def activeCB(self, msg):
        self.active = msg.data

    def controllerCB(self, msg, response):
        try:
            with self.mutex:
                self.state = msg.state
                print(f"recv: {self.state}")
                for i in range(3):
                    self.params[i] = getattr(msg, f"team{i}")
            response.success = True
        except Exception as e:
            print(f"Error: {str(e)}")
            response.success = False
        return response

    def settingsCB(self, msg: Settings):
        global TEAM_GOAL, OP_GOAL, ATTRACTIVE_GAIN, REPULSIVE_GAIN, REPULSION_RADIUS, TANGENTIAL_GAIN, GOAL_TOLERANCE, USE_LOCAL, TARGET_OFFSET, COLINEARITY, DEF_POS
        if msg.team_side:
            TEAM_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
            OP_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
            DEF_POS = np.array([(FIELD_LENGTH - 4) / 2, 0.0])
        else:
            TEAM_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
            OP_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
            DEF_POS = np.array([-(FIELD_LENGTH - 4) / 2, 0.0])

        ATTRACTIVE_GAIN = msg.attractive_gain
        REPULSIVE_GAIN = msg.repulsive_gain
        REPULSION_RADIUS = msg.repulsion_radius
        TANGENTIAL_GAIN = msg.tangential_gain
        GOAL_TOLERANCE = msg.goal_tolerance
        TARGET_OFFSET = msg.target_offset
        COLINEARITY = msg.colinearity
        USE_LOCAL = msg.local
        self.mapping = [msg.robot0, msg.robot1, msg.robot2]

    def send(self):
        if self.state == State.HALT:
            return
        for i, cmd in enumerate(self.cmds):
            if cmd is not None:
                self.cmd_publishers[i].publish(cmd)
        for i, tgt in enumerate(self.tgts):
            if tgt is not None:
                self.tgt_publishers[i].publish(tgt)

    def roleAssigner(self, field):
        defender = -1
        midfield = []
        best = 999
        for i in range(3):
            robot = getattr(field, f"team{i}")
            robot_coords = np.array([robot.x, robot.y])
            dist = np.linalg.norm(TEAM_GOAL - robot_coords)
            if dist < best:
                best = dist
                defender = i

        ball_coords = np.array([field.ball.x, field.ball.y])
        attacker = self.current_attacker

        if ball_coords[0] == 999:
            attacker = -1
            self.attacker_challenger = -1
            for i in range(3):
                if i != defender:
                    midfield.append(i)
        else:
            dists = {}
            for i in range(3):
                if i == defender:
                    continue
                robot = getattr(field, f"team{i}")
                dists[i] = np.linalg.norm(ball_coords - np.array([robot.x, robot.y]))

            if not dists:
                attacker = -1
                self.attacker_challenger = -1
            else:
                closest = min(dists, key=dists.get)
                if attacker not in dists:
                    attacker = closest
                    self.attacker_challenger = -1
                elif closest != attacker and (dists[attacker] - dists[closest]) > ATTACKER_SWAP_MARGIN:
                    now = time.time()
                    if self.attacker_challenger != closest:
                        self.attacker_challenger = closest
                        self.challenger_since = now
                    elif now - self.challenger_since > ATTACKER_SWAP_DWELL:
                        attacker = closest
                        self.attacker_challenger = -1
                else:
                    self.attacker_challenger = -1

            for i in range(3):
                if i != defender and i != attacker:
                    midfield.append(i)

        self.current_attacker = attacker
        return attacker, midfield, defender

    def predPos(self, obj, horizon, friction=0.0):
        vx, vy = obj.vx, obj.vy
        v = math.hypot(vx, vy)
        if v == 0:
            return obj.x, obj.y
        if friction <= 0:
            return obj.x + vx * horizon, obj.y + vy * horizon
        t_stop = v / friction
        if horizon >= t_stop:
            d = v * t_stop - 0.5 * friction * t_stop ** 2
        else:
            d = v * horizon - 0.5 * friction * horizon ** 2
        dir_x, dir_y = vx / v, vy / v
        return obj.x + dir_x * d, obj.y + dir_y * d

    def _enemy_positions(self, field):
        enemies = []
        for i in range(3):
            op = getattr(field, f"op{i}")
            if op.x == 999:
                continue
            enemies.append(np.array([op.x, op.y]))
        return enemies

    def gpCB(self, field: FieldData):
        with self.mutex:
            state = self.state
            params = list(self.params)

        match state:
            case State.PAUSE:
                for i in range(3):
                    self.cmds[i] = LowCmd(robot_id=i, vx=0., vy=0., dtheta=0.)

            case State.PLAY:
                attacker, midfield, defender = self.roleAssigner(field)
                enemies = self._enemy_positions(field)

                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = LowCmd(robot_id=i, vx=0., vy=0., dtheta=0.)
                        continue

                    team_obj = getattr(field, f"team{team_index}")
                    if team_obj.x == 999:
                        self.cmds[i] = LowCmd(robot_id=i, vx=0., vy=0., dtheta=0.)
                        continue

                    ball_coords = np.array([field.ball.x, field.ball.y])
                    team_coords = np.array([team_obj.x, team_obj.y])

                    if team_index == attacker:
                        horizon = np.linalg.norm(ball_coords - team_coords)
                        if horizon < ATTACKER_LOOKAHEAD_MIN_DIST:
                            future_ball_pos = ball_coords
                        else:
                            future_ball_pos = np.array(self.predPos(field.ball, horizon, BALL_FRICTION))

                        if ball_coords[1] > FIELD_LIMS[1] - 2 or ball_coords[1] < -FIELD_LIMS[1] + 2:
                            self.cmds[i], pos = self.skills.moveToStrike(
                                team_obj, ball_coords, 0., [],
                                np.array([np.copysign(1, OP_GOAL[0]), 0]))
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)
                        else:
                            aim_point = pick_aim_point(ball_coords, OP_GOAL, GOAL_WIDTH, enemies)
                            vec = aim_point - ball_coords
                            norm_vec = _unit(vec)
                            if np.linalg.norm(norm_vec) < 1e-6:
                                norm_vec = _unit(OP_GOAL - ball_coords)
                            self.cmds[i], pos = self.skills.moveToStrike(team_obj, future_ball_pos, 0., [], norm_vec)
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)

                    elif team_index in midfield:
                        horizon = np.linalg.norm(ball_coords - team_coords)
                        if horizon < ATTACKER_LOOKAHEAD_MIN_DIST:
                            future_ball_pos = ball_coords
                        else:
                            future_ball_pos = np.array(self.predPos(field.ball, horizon, BALL_FRICTION))

                        if ball_coords[0] == 999:
                            self.cmds[i], _ = self.skills.moveToPoint(team_obj, MID_POS[midfield.index(team_index)], 0, [])
                        elif math.copysign(1, ball_coords[0]) == math.copysign(1, OP_GOAL[0]):
                            y = (future_ball_pos[1] - TEAM_GOAL[1]) / 2
                            x = np.copysign(4, TEAM_GOAL[0])
                            self.cmds[i], _ = self.skills.moveToPoint(team_obj, np.array([x, y]), 0., [])
                        else:
                            aim_point = pick_aim_point(ball_coords, OP_GOAL, GOAL_WIDTH, enemies)
                            vec = aim_point - ball_coords
                            norm_vec = _unit(vec)
                            if np.linalg.norm(norm_vec) < 1e-6:
                                norm_vec = _unit(OP_GOAL - ball_coords)
                            self.cmds[i], pos = self.skills.moveToStrike(team_obj, future_ball_pos, 0., [], norm_vec)
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)

                    elif team_index == defender:
                        if ball_coords[0] == 999:
                            self.cmds[i], _ = self.skills.moveToPointOrg(team_obj, DEF_POS, 0., [])
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=DEF_POS[1], tgt_theta=0.)
                        else:
                            dist1 = np.linalg.norm(team_coords - ball_coords)
                            lim = np.clip(ball_coords[1], -3, 3)
                            dist2 = np.linalg.norm(team_coords - np.array([DEF_POS[0], lim]))
                            angle = -90.0
                            if dist1 < 2 and dist2 < 2:
                                aim_point = pick_aim_point(ball_coords, OP_GOAL, GOAL_WIDTH, enemies)
                                vec = aim_point - ball_coords
                                norm_vec = _unit(vec)
                                if np.linalg.norm(norm_vec) < 1e-6:
                                    norm_vec = _unit(OP_GOAL - ball_coords)
                                self.cmds[i], pos = self.skills.moveToStrikeOrg(
                                    team_obj, ball_coords + norm_vec * TARGET_OFFSET, angle, [], norm_vec)
                                self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=angle)
                            elif dist1 > 10:
                                self.cmds[i], _ = self.skills.moveToPointOrg(team_obj, DEF_POS, angle, [])
                                self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=DEF_POS[1], tgt_theta=angle)
                            else:
                                if abs(field.ball.vx) < 0.1:
                                    horizon = 0
                                else:
                                    horizon = abs((DEF_POS[0] - ball_coords[0]) / field.ball.vx)
                                future_ball_pos = self.predPos(field.ball, horizon, BALL_FRICTION)
                                y = np.clip(future_ball_pos[1], -3, 3)
                                self.cmds[i], _ = self.skills.moveToPointOrg(team_obj, np.array([DEF_POS[0], y]), angle, [])
                                self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=y, tgt_theta=angle)
                    else:
                        self.cmds[i] = LowCmd(robot_id=i, vx=0., vy=0., dtheta=0.)


def main(args=None):
    rclpy.init(args=args)
    node = Strat()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
