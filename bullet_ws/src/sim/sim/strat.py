import rclpy
import numpy as np
from rclpy.node import Node
from sim_msgs.msg import FieldData, LowCmd, HighCmd, ObjData, Settings
from sim_msgs.srv import Controller
from enum import IntEnum
import threading

class State(IntEnum):
    PAUSE = 0
    PLAY = 1
    MIDFIELD = 2
    PENALTY = 3

FIELD_LENGTH = 17
TEAM_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
OP_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])

ATTRACTIVE_GAIN = 0.5
REPULSIVE_GAIN = 3
REPULSION_RADIUS = 1
GOAL_TOLERANCE = 1
TANGENTIAL_GAIN = 3
MAX_LINEAR_SPEED = 3

USE_LOCAL = True

class SkillLib:
    def moveToPoint(self, robot: ObjData, target_pos: np.ndarray, target_theta: float, obstacles: list[ObjData]) -> LowCmd:
        robot_pos = np.array([robot.x, robot.y])
        robot_vel = np.array([robot.vx, robot.vy])
        net_vector = self._calculate_potential_field_vector(robot_pos, robot_vel, target_pos, obstacles)
        if USE_LOCAL:
            vx_robot, vy_robot = self._world_to_robot_frame(net_vector, robot.theta)
        else:
            vx_robot, vy_robot = net_vector

        vx_capped, vy_capped = self._cap_speed(vx_robot, vy_robot)
        cmd = LowCmd()
        cmd.robot_id = robot.obj_id
        cmd.vx = vx_capped
        cmd.vy = vy_capped
        if abs(-robot.theta + target_theta) < (360 -robot.theta + target_theta) % 360:
            cmd.dtheta = -robot.theta + target_theta
        else:
            cmd.dtheta = (360 - robot.theta + target_theta) % 360

        return cmd
    
    def strikeBall(self, robot: ObjData, ball: ObjData, strike_target_pos: np.ndarray) -> LowCmd:
        vec_ball_to_target = strike_target_pos - np.array([ball.x, ball.y])
        
        drive_through_point = np.array([ball.x, ball.y]) + 0.1 * (vec_ball_to_target / np.linalg.norm(vec_ball_to_target))

        strike_theta = np.rad2deg(np.arctan2(vec_ball_to_target[1], vec_ball_to_target[0]) + 90)
        
        cmd = self.moveToPoint(robot, drive_through_point, strike_theta, obstacles=[])
        return cmd

    def _calculate_potential_field_vector(self, robot_pos: np.ndarray, robot_vel: np.ndarray, target_pos: np.ndarray, obstacles: list[ObjData]) -> np.ndarray:
        attractive_vector = ATTRACTIVE_GAIN * (target_pos - robot_pos)
        if np.linalg.norm(target_pos - robot_pos) < GOAL_TOLERANCE:
            return attractive_vector

        net_repulsive_vector = np.array([0.0, 0.0])
        for obs in obstacles:
            obs_pos = np.array([obs.x, obs.y])
            vec_to_robot = robot_pos - obs_pos
            dist_to_robot = np.linalg.norm(vec_to_robot)
            
            if dist_to_robot < REPULSION_RADIUS:
                repulsion_magnitude = REPULSIVE_GAIN * (1.0 / dist_to_robot - 1.0 / REPULSION_RADIUS)
                radial_repulsive_force = repulsion_magnitude * (vec_to_robot / dist_to_robot)
                vec_robot_to_goal = target_pos - robot_pos
                tangential_dir = np.array([-vec_robot_to_goal[1], vec_robot_to_goal[0]])
                if np.dot(tangential_dir, vec_to_robot) < 0:
                    tangential_dir = -tangential_dir
                
                tangential_force = TANGENTIAL_GAIN * repulsion_magnitude * (tangential_dir / np.linalg.norm(tangential_dir))
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
        if speed > MAX_LINEAR_SPEED:
            scale_factor = MAX_LINEAR_SPEED / speed
            return vx * scale_factor, vy * scale_factor
        return vx, vy

class Strat(Node):
    def __init__(self):
        super().__init__('strat')
        self.skills = SkillLib()
        
        self.field_subscriber = self.create_subscription(FieldData, 'field_data', self.gpCB, 10)
        self.settings_subscriver = self.create_subscription(Settings, 'settings', self.settingsCB, 10)
        self.controller_service = self.create_service(Controller, 'strat/controller', self.controllerCB)
        
        self.cmd_publishers = {
            0: self.create_publisher(LowCmd, '/low0', 10),
            1: self.create_publisher(LowCmd, '/low1', 10),
            2: self.create_publisher(LowCmd, '/low2', 10)
        }
        
        self.get_logger().info("Strategist node initialized.")
        self.cmds = [None, None, None]
        self.timer = self.create_timer(0.1, self.send)

        self.state = 0
        self.mod = 0
        self.params = [HighCmd, HighCmd, HighCmd]
        self.mapping = [-1, -1, -1]

        self.mutex = threading.Lock()
        
    
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
        global TEAM_GOAL, OP_GOAL, ATTRACTIVE_GAIN, REPULSIVE_GAIN, REPULSION_RADIUS, TANGENTIAL_GAIN, GOAL_TOLERANCE, USE_LOCAL
        if msg.team_side:
            TEAM_GOAL = np.array([FIELD_LENGTH / 2, 0.0])
            OP_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
        else:
            TEAM_GOAL = np.array([-FIELD_LENGTH / 2, 0.0])
            OP_GOAL = np.array([FIELD_LENGTH / 2, 0.0])

        ATTRACTIVE_GAIN = msg.attractive_gain
        REPULSIVE_GAIN = msg.repulsive_gain
        REPULSION_RADIUS = msg.repulsive_gain
        TANGENTIAL_GAIN = msg.tangential_gain
        GOAL_TOLERANCE = msg.goal_tolerance

        USE_LOCAL = msg.local

        self.mapping = [msg.robot0, msg.robot1, msg.robot2]

    def send(self):
        for i, cmd in enumerate(self.cmds):
            if cmd is not None:
                self.cmd_publishers[i].publish(cmd)

    def gpCB(self, field: FieldData): 
        with self.mutex:
            state = self.state
            mod = self.mod
            params = list(self.params)
        
        match state:
            case State.PAUSE:
                cmd = LowCmd(robot_id=0, vx=0., vy=0., dtheta=0.)
                for i in range(3):
                    self.cmds[i] = cmd

            case State.PLAY:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")

                    target = [
                        np.array([0, 0]),
                        np.array([0, 0]),
                        np.array([0, 0]),
                    ][i]

                    self.cmds[i] = self.skills.moveToPoint(team_obj, target, 0., [])

                #self.cmds[0] = self.skills.moveToPoint(field.team0, np.array([3, 3]), 0., [])
                #self.cmds[1] = self.skills.moveToPoint(field.team1, np.array([0, 0]), 0., [])
                #self.cmds[2] = self.skills.moveToPoint(field.team2, np.array([3, -3]), 0., [])

            case State.MIDFIELD:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")

                    target = [
                        np.array([3, 2]),
                        np.array([3, -2]),
                        TEAM_GOAL,
                    ][i]

                    self.cmds[i] = self.skills.moveToPoint(team_obj, target, 0., [])

            case State.PENALTY:
                for i, team_index in enumerate(self.mapping):
                    if team_index == -1:
                        self.cmds[i] = None
                        continue

                    team_obj = getattr(field, f"team{team_index}")

                    target = [
                        np.array([-1, 2]),
                        np.array([-1, -2]),
                        TEAM_GOAL,
                    ][i]

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