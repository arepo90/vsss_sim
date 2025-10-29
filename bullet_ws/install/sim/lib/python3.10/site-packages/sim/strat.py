import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from sim_msgs.msg import FieldData, LowCmd, HighCmd, ObjData, Settings
from sim_msgs.srv import Controller
from enum import IntEnum
import threading
import math

class State(IntEnum):
    HALT = -1
    PAUSE = 0
    PLAY = 1
    MIDFIELD_DEF = 2
    PENALTY_DEF = 3
    MIDFIELD_ATT = 4
    PENALTY_ATT = 5

FIELD_LENGTH = 17
FIELD_HEIGHT = 13
GOAL_WIDTH = 3
TEAM_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
OP_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
DEF_POS = np.array([(FIELD_LENGTH-4) / 2, 0.0])
MID_POS = [np.array([0, 3]), np.array([0, -3]), np.array([0, 0])]
FIELD_LIMS = np.array([7, 6])

PENALTY_POS_DEF = [DEF_POS,
                np.array([-1, 3]),
                np.array([-1, -3])]

PENALTY_POS_ATT = [DEF_POS,
                   np.array([-1, 3]),
                   np.array([3, 0])]

MIDFIELD_POS_DEF = [DEF_POS,
                    np.array([5, 3]),
                    np.array([5, -3])]

MIDFIELD_POS_ATT = [DEF_POS,
                    np.array([5, 3]),
                    np.array([5, -3])]

X_MARGIN = 2
Y_MARGIN = 1

ATTRACTIVE_GAIN = 0.5
REPULSIVE_GAIN = 2
REPULSION_RADIUS = 1
GOAL_TOLERANCE = 1
TANGENTIAL_GAIN = 3
TARGET_OFFSET = 0.5
COLINEARITY = 0.975
APPROACH_DISTANCE = 1
DEFENSE_DISTANCE_FROM_GOAL = 1.5
KICK_TRIGGER_DISTANCE = 2

USE_LOCAL = True

def intersects(ball, robot):
    rx, ry = robot
    bx, by = ball
    goal_y_min = -GOAL_WIDTH / 2
    goal_y_max = GOAL_WIDTH / 2
    dx = bx - rx
    dy = by - ry
    if dx == 0:
        return rx == TEAM_GOAL[0]

    shot_direction_x = dx
    goal_direction_x = -TEAM_GOAL[0] - rx
    if (shot_direction_x * goal_direction_x) <= 0:
        print("False")
        return False

    m = dy / dx
    y_hit = ry + m * (-TEAM_GOAL[0] - rx)
    return goal_y_min <= y_hit <= goal_y_max

class SkillLib:
    def moveToPoint(self, robot: ObjData, target_pos: np.ndarray, target_theta: float, obstacles: list[np.ndarray], bypass = False) -> LowCmd:
        robot_pos = np.array([robot.x, robot.y])
        robot_vel = np.array([robot.vx, robot.vy])
        target_pos = np.clip(target_pos, -FIELD_LIMS, FIELD_LIMS)
        net_vector = self._calculate_potential_field_vector(robot_pos, robot_vel, target_pos, obstacles, bypass)
        if USE_LOCAL:
            vx_robot, vy_robot = self._world_to_robot_frame(net_vector, robot.theta)
        else:
            vx_robot, vy_robot = net_vector

        vx_capped, vy_capped = self._cap_speed(vx_robot, vy_robot)
        cmd = LowCmd()
        cmd.robot_id = robot.obj_id
        cmd.vx = vx_capped
        cmd.vy = vy_capped

        """
        if abs(-robot.theta + target_theta) < (360 -robot.theta + target_theta) % 360:
            cmd.dtheta = -robot.theta + target_theta
        else:
            cmd.dtheta = (360 - robot.theta + target_theta) % 360
        """
        cmd.dtheta = theta = (target_theta - robot.theta + 180) % 360 - 180
        return cmd, target_pos
    
    def moveToStrike(self, robot: ObjData, target_pos: np.ndarray, target_theta: float, obstacles: list[np.ndarray], strike_dir: np.ndarray) -> LowCmd:
        robot_pos = np.array([robot.x, robot.y])
        vec_robot_to_target = target_pos - robot_pos
        dist_to_target = np.linalg.norm(vec_robot_to_target)
        if dist_to_target < 1e-6:
            alignment = 1.0
        else:
            norm_vec_robot_to_target = vec_robot_to_target / dist_to_target
            alignment = np.dot(norm_vec_robot_to_target, strike_dir)

        #inter = intersects(target_pos, robot_pos)
        
        if alignment > COLINEARITY:
            return self.moveToPoint(robot, target_pos + strike_dir * TARGET_OFFSET, target_theta, [])
        else:
            return self.moveToPoint(robot, target_pos - strike_dir * TARGET_OFFSET, target_theta, obstacles + [target_pos], True)
        
        """
        if alignment < -0.5:
            return self.moveToPoint(robot, target_pos - strike_dir * TARGET_OFFSET, target_theta, obstacles + [target_pos], True), target_pos - strike_dir * TARGET_OFFSET
        elif alignment > COLINEARITY:
            return self.moveToPoint(robot, target_pos + strike_dir * TARGET_OFFSET, target_theta, obstacles, True), target_pos + strike_dir * TARGET_OFFSET
        else:
            return self.moveToPoint(robot, target_pos - strike_dir * TARGET_OFFSET, target_theta, obstacles, True), target_pos - strike_dir * TARGET_OFFSET
        """

    def _calculate_potential_field_vector(self, robot_pos: np.ndarray, robot_vel: np.ndarray, target_pos: np.ndarray, obstacles: list[np.ndarray], bypass = False) -> np.ndarray:
        
        dist = np.linalg.norm(target_pos - robot_pos)
        if dist < 1e-6:
            return np.array([0., 0.])
        
        #attractive_vector = ATTRACTIVE_GAIN * (target_pos - robot_pos)
        #norm_vec = (target_pos - robot_pos) / np.linalg.norm(target_pos - robot_pos)
        #attractive_vector = ATTRACTIVE_GAIN * norm_vec
        
        direction = target_pos - robot_pos
        distance = np.linalg.norm(direction)
        if distance < 1e-6:
            return np.array([0., 0.])

        direction /= distance

        v_max = ATTRACTIVE_GAIN
        d0 = GOAL_TOLERANCE 
        n = 2

        mag = v_max * (distance**n) / (distance**n + d0**n + 1e-9)
        attractive_vector = direction * mag

        net_repulsive_vector = np.array([0.0, 0.0])
        for obs in obstacles:
            vec_to_robot = robot_pos - obs
            dist_to_robot = np.linalg.norm(vec_to_robot)
            if dist_to_robot < REPULSION_RADIUS:
                vec_robot_to_goal = target_pos - robot_pos
                if not bypass:
                    repulsion_magnitude = REPULSIVE_GAIN * (1.0 / dist_to_robot - 1.0 / REPULSION_RADIUS)
                    radial_repulsive_force = repulsion_magnitude * (vec_to_robot / dist_to_robot)
                else:
                    repulsion_magnitude = REPULSIVE_GAIN * (1.0 / dist_to_robot - 1.0 / REPULSION_RADIUS)
                    radial_repulsive_force = 0

                tangential_dir = np.array([-vec_robot_to_goal[1], vec_robot_to_goal[0]])
                if np.dot(tangential_dir, vec_to_robot) < 0:
                    tangential_dir = -tangential_dir

                norm_tangential_dir = np.linalg.norm(tangential_dir)
                if norm_tangential_dir > 1e-6:
                    tangential_force = TANGENTIAL_GAIN * repulsion_magnitude * (tangential_dir / norm_tangential_dir)
                    #tangential_force = TANGENTIAL_GAIN * (tangential_dir / norm_tangential_dir)
                else:
                    tangential_force = np.array([0., 0.])

                #tangential_force = TANGENTIAL_GAIN * repulsion_magnitude * (tangential_dir / np.linalg.norm(tangential_dir))
                net_repulsive_vector += (radial_repulsive_force + tangential_force)

        return attractive_vector + net_repulsive_vector

    def _world_to_robot_frame(self, vector: np.ndarray, robot_theta_deg: float) -> tuple[float, float]:
        theta_rad = np.deg2rad(-robot_theta_deg)
        c, s = np.cos(theta_rad), np.sin(theta_rad)
        vx_world, vy_world = vector[0], vector[1]    
        vx_robot = c * vx_world + s * vy_world
        vy_robot = -s * vx_world + c * vy_world
        return vx_robot, vy_robot
        
    def _cap_speed(self, vx: float, vy: float) -> tuple[float, float]:
        speed = np.sqrt(vx**2 + vy**2)
        if speed > 1:
            scale_factor = 1 / speed
            return vx * scale_factor, vy * scale_factor
        
        return vx, vy

class Strat(Node):
    def __init__(self):
        super().__init__('strat')
        self.skills = SkillLib()
        
        self.field_subscriber = self.create_subscription(FieldData, 'field_data', self.gpCB, 10)
        self.settings_subscriber = self.create_subscription(Settings, 'settings', self.settingsCB, 10)
        self.active_subscriber = self.create_subscription(Int32MultiArray, 'active', self.activeCB, 10)
        self.controller_service = self.create_service(Controller, 'strat/controller', self.controllerCB)
        
        self.cmd_publishers = {
            0: self.create_publisher(LowCmd, '/low0', 10),
            1: self.create_publisher(LowCmd, '/low1', 10),
            2: self.create_publisher(LowCmd, '/low2', 10)
        }
        self.tgt_publishers = {
            0: self.create_publisher(HighCmd, '/high0', 10),
            1: self.create_publisher(HighCmd, '/high1', 10),
            2: self.create_publisher(HighCmd, '/high2', 10)
        }
        
        self.get_logger().info("Strategist node initialized.")
        self.cmds = [None, None, None]
        self.tgts = [None, None, None]
        self.timer = self.create_timer(0.1, self.send)

        self.state = 0
        self.mod = 0
        self.params = [HighCmd, HighCmd, HighCmd]
        self.mapping = [-1, -1, -1]
        self.active = [0, 0, 0]
        self.mutex = threading.Lock()

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
            DEF_POS = np.array([(FIELD_LENGTH-4) / 2, 0.0])
        else:
            TEAM_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
            OP_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
            DEF_POS = np.array([-(FIELD_LENGTH-4) / 2, 0.0])

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

    def isInRegion(self, obj, region):
        if region[0] <= obj[0] <= region[2] and region[1] <= obj[1] <= region[3]:
            return True
        
        return False

    def roleAssigner(self, field):
        defender = -1
        midfield = []
        attacker = -1
        best = 999
        for i in range(3):
            robot = getattr(field, f"team{i}")
            robot_coords = np.array([robot.x, robot.y])
            dist = np.linalg.norm(TEAM_GOAL - robot_coords)
            #if dist < best and self.active[i]:
            if dist < best:
                best = dist
                defender = i

        ball_coords = np.array([field.ball.x, field.ball.y])
        best = 999
        if ball_coords[0] == 999:
            for i in range(3):
                if i != defender:
                    midfield.append(i)                
        #elif math.copysign(1, ball_coords[0]) == math.copysign(1, OP_GOAL[0]):
        elif np.linalg.norm(ball_coords - OP_GOAL) < 15:
            for i in range(3):
                robot = getattr(field, f"team{i}")
                robot_coords = np.array([robot.x, robot.y])
                dist = np.linalg.norm(ball_coords - robot_coords)
                #if dist < best and i != defender and self.active[i]:
                if dist < best and i != defender:
                    best = dist
                    attacker = i

            for i in range(3):
                #if defender != i and attacker != i and self.active[i]:
                if defender != i and attacker != i:
                    midfield.append(i)
        else:
            for i in range(3):
                #if defender != i and self.active[i]:
                if defender != i:
                    midfield.append(i)

        return attacker, midfield, defender
    
    def predPos(self, obj, horizon, friction=0.0):
        vx, vy = obj.vx, obj.vy
        v = math.hypot(vx, vy)
        if v == 0:
            return obj.x, obj.y

        if friction <= 0:
            x_pred = obj.x + vx * horizon
            y_pred = obj.y + vy * horizon
            return x_pred, y_pred

        t_stop = v / friction
        if horizon >= t_stop:
            d = v * t_stop - 0.5 * friction * t_stop**2
        else:
            d = v * horizon - 0.5 * friction * horizon**2

        dir_x, dir_y = vx / v, vy / v
        x_pred = obj.x + dir_x * d
        y_pred = obj.y + dir_y * d
        return x_pred, y_pred

    def getAngle(self, ball_coords, robot_coords):
        vec = ball_coords - robot_coords
        theta = math.atan2(vec[1], vec[0])
        angle = - (theta - math.pi/2)
        angle_deg = math.degrees(angle)
        return angle_deg
    
    def allButSelf(self, field, robot, team_only = True):
        all = []
        for i in range(6):
            if i < 3:
                obj = getattr(field, f"team{i}")
                if obj != robot:
                    all.append(np.array([obj.x, obj.y]))
            elif not team_only:
                obj = getattr(field, f"op{i%3}")
                all.append(np.array([obj.x, obj.y]))

        return all

    def gpCB(self, field: FieldData): 
        with self.mutex:
            state = self.state
            mod = self.mod
            params = list(self.params)
        
        match state:
            case State.PAUSE:
                for i in range(3):
                    self.cmds[i] = LowCmd(robot_id=i, vx=0., vy=0., dtheta=0.)
                
            case State.PLAY:
                attacker, midfield, defender = self.roleAssigner(field)
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
                        if horizon < 2:
                            future_ball_pos = ball_coords
                        else:
                            future_ball_pos = self.predPos(field.ball, horizon, 3) # mod
                        #inter = self.intersects(future_ball_pos, team_coords)

                        if ball_coords[1] > FIELD_LIMS[1] - 2 or ball_coords[1] < -FIELD_LIMS[1] + 2:
                            print("margin")
                            self.cmds[i], pos = self.skills.moveToStrike(team_obj, ball_coords, 0., [], np.array([-1, 0]))
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)
                        else:
                            vec = OP_GOAL - ball_coords
                            norm_vec = vec / np.linalg.norm(vec)
                            self.cmds[i], pos = self.skills.moveToStrike(team_obj, future_ball_pos, 0., [ball_coords], norm_vec)
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)
                        """
                        print(inter)
                        if inter:
                            angle = 0.0
                            #self.cmds[i] = self.skills.moveToPoint(team_obj, future_ball_pos, angle, [])
                            vec = OP_GOAL - ball_coords
                            norm_vec = vec / np.linalg.norm(vec)
                            self.cmds[i] = self.skills.moveToStrike(team_obj, future_ball_pos + norm_vec * TARGET_OFFSET, 0., [], norm_vec)
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=future_ball_pos[0], tgt_y=future_ball_pos[1], tgt_theta=angle)
                        else:
                            vec = OP_GOAL - future_ball_pos
                            norm_vec = vec / np.linalg.norm(vec)
                            pos = future_ball_pos - norm_vec * TARGET_OFFSET
                            self.cmds[i] = self.skills.moveToPoint(team_obj, pos, 0., [])
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)
                        """

                        """
                        horizon = np.linalg.norm(ball_coords - team_coords)
                        future_ball_pos = self.predPos(field.ball, horizon)
                        vec = TEAM_GOAL - future_ball_pos
                        norm_vec = vec / np.linalg.norm(vec)
                        self.cmds[i] = self.skills.moveToStrike(team_obj, future_ball_pos + norm_vec * TARGET_OFFSET, 0., [], norm_vec)
                        """
                        
                    elif team_index in midfield:
                        if ball_coords[0] == 999:
                            self.cmds[i], _ = self.skills.moveToPoint(team_obj, MID_POS[midfield.index(team_index)], 0, [])
                        if math.copysign(1, ball_coords[0]) == math.copysign(1, OP_GOAL[0]):
                            y = (ball_coords[1] - TEAM_GOAL[1]) / 2
                            x = np.copysign(4, TEAM_GOAL[0])
                            self.cmds[i], _ = self.skills.moveToPoint(team_obj, np.array([x, y]), 0., [])
                        else:
                            horizon = np.linalg.norm(ball_coords - team_coords)
                            future_ball_pos = self.predPos(field.ball, horizon) # mod
                            #inter = self.intersects(future_ball_pos, team_coords)
                            angle = 0.0
                            vec = OP_GOAL - ball_coords
                            norm_vec = vec / np.linalg.norm(vec)
                            self.cmds[i], pos = self.skills.moveToStrike(team_obj, future_ball_pos + norm_vec * TARGET_OFFSET, 0., [self.allButSelf(field, team_obj)], norm_vec)
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=0.)
                    elif team_index == defender:
                        if ball_coords[0] == 999:
                            self.cmds[i], _ = self.skills.moveToPoint(team_obj, DEF_POS, 0., [])
                            self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=DEF_POS[1], tgt_theta=0.)
                        else:
                            dist1 = np.linalg.norm(team_coords - ball_coords)
                            lim = np.clip(ball_coords[1], -3, 3)
                            dist2 = np.linalg.norm(team_coords - np.array([DEF_POS[0], lim]))
                            angle = -90.0
                            print(dist1, dist2)
                            if dist1 < 2 and dist2 < 2: # kick
                                #angle = 0.0
                                vec = ball_coords - TEAM_GOAL
                                norm_vec = vec / np.linalg.norm(vec)
                                pos = ball_coords + norm_vec * TARGET_OFFSET
                                #self.cmds[i] = self.skills.moveToPoint(team_obj, pos, angle, [])
                                self.cmds[i], pos = self.skills.moveToStrike(team_obj, ball_coords + norm_vec * TARGET_OFFSET, angle, [], norm_vec)
                                self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=angle)
                                """
                                elif  abs(ball_coords[0]) >= abs(team_coords[0]):
                                    vec = team_coords - ball_coords
                                    norm_vec = vec / np.linalg.norm(vec)
                                    pos = ball_coords + norm_vec * TARGET_OFFSET
                                    #self.cmds[i] = self.skills.moveToPoint(team_obj, pos, angle, [])
                                    self.cmds[i] = self.skills.moveToStrike(team_obj, ball_coords + norm_vec * TARGET_OFFSET, angle, [], norm_vec)
                                    self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=pos[0], tgt_y=pos[1], tgt_theta=angle)
                                """
                                """
                                elif abs(ball_coords[0] - DEF_POS[0]) < 2: # close
                                    if abs(ball_coords[1]) > 3:
                                        y = np.copysign(3, ball_coords[1])
                                    else:
                                        y = ball_coords[1]
                                    self.cmds[i] = self.skills.moveToPoint(team_obj, np.array([DEF_POS[0], y]), angle, [])
                                    self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=y, tgt_theta=angle)
                                """
                            elif dist1 > 10: # far
                                #angle = self.getAngle(ball_coords, team_coords)
                                self.cmds[i], _ = self.skills.moveToPoint(team_obj, DEF_POS, angle, [])
                                self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=DEF_POS[1], tgt_theta=angle)
                            else: # follow
                                #angle = self.getAngle(ball_coords, team_coords)
                                if abs(field.ball.vx) < 0.1:
                                    horizon = 0
                                else:
                                    horizon = abs((DEF_POS[0] - ball_coords[0]) / field.ball.vx)
                                future_ball_pos = self.predPos(field.ball, horizon, 3)
                                """
                                if abs(future_ball_pos[1]) > 3:
                                    y = np.copysign(3, future_ball_pos[1])
                                else:
                                    y = future_ball_pos[1]
                                """
                                y = np.clip(future_ball_pos[1], -3, 3)
                                self.cmds[i], _ = self.skills.moveToPoint(team_obj, np.array([DEF_POS[0], y]), angle, [])
                                self.tgts[i] = HighCmd(robot_id=i, skill=0, mod=0, tgt_x=DEF_POS[0], tgt_y=y, tgt_theta=angle)
                                #y = ball_coords[1] * GOAL_WIDTH / FIELD_HEIGHT
                                #self.cmds[i] = self.skills.moveToPoint(team_obj, np.array([DEF_POS[0], y]), angle, [])

                            """
                            vec = ball_coords - TEAM_GOAL
                            norm_vec = vec / np.linalg.norm(vec)
                            dist1 = np.linalg.norm(team_coords - ball_coords)
                            dist2 = np.linalg.norm(team_coords - TEAM_GOAL)
                            if dist1 < 2 and dist2 < 2:
                                self.cmds[i] = self.skills.moveToStrike(team_obj, ball_coords + norm_vec * TARGET_OFFSET, 0., [], norm_vec)
                            else:
                                self.cmds[i] = self.skills.moveToPoint(team_obj, TEAM_GOAL + norm_vec * 1, 0, [])
                            """
                    else:
                        self.cmds[i] = LowCmd(robot_id=i, vx=0., vy=0., dtheta=0.)

            case State.MIDFIELD_DEF:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")
                    target = MIDFIELD_POS_DEF[i]

                    self.cmds[i] = self.skills.moveToPoint(team_obj, target, 0., [])

            case State.PENALTY_DEF:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")

                    target = PENALTY_POS_DEF[i]

                    self.cmds[i] = self.skills.moveToPoint(team_obj, target, 0., [])

            case State.MIDFIELD_ATT:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")
                    target = MIDFIELD_POS_ATT[i]

                    self.cmds[i] = self.skills.moveToPoint(team_obj, target, 0., [])

            case State.PENALTY_ATT:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")

                    target = PENALTY_POS_ATT[i]

                    self.cmds[i] = self.skills.moveToPoint(team_obj, target, 0., [])
  

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