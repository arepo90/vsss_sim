import rclpy
import numpy as np
from rclpy.node import Node
from sim_msgs.msg import FieldData, LowCmd, ObjData

FIELD_LENGTH = 17
MY_GOAL_POS = np.array([FIELD_LENGTH / 2, 0.0])
OPPONENT_GOAL_POS = np.array([-FIELD_LENGTH / 2, 0.0])

class Obstacle:
    def __init__(self, x, y, radius = 0.4):
        self.pos = np.array([x, y])
        self.radius = radius

# esta clase realmente no es la Skill Library de la que hablamos, por ahora ignorenla jaja
class SkillLib:
    def __init__(self):
        self.ATTRACTIVE_GAIN = 0.5 # 8
        self.DAMPING_GAIN = 1
        self.REPULSIVE_GAIN = 5
        self.REPULSION_RADIUS = 4
        self.MAX_LINEAR_SPEED = 3.0
        self.ROBOT_RADIUS = 0.4
        
    def moveToPoint(self, robot: ObjData, target_pos: np.ndarray, target_theta: float, obstacles: list[Obstacle]) -> LowCmd:
        robot_pos = np.array([robot.x, robot.y])
        robot_vel = np.array([robot.vx, robot.vy])

        #net_vector = self._calculate_potential_field_vector(robot_pos, robot_vel, target_pos, obstacles)
        #vx_robot, vy_robot = self._world_to_robot_frame(net_vector, robot.theta)

        vx_robot, vy_robot = self._calculate_potential_field_vector(robot_pos, robot_vel, target_pos, obstacles)
        
        vx_capped, vy_capped = self._cap_speed(vx_robot, vy_robot)

        cmd = LowCmd()
        cmd.robot_id = robot.obj_id
        cmd.vx = vx_capped
        cmd.vy = vy_capped
        #cmd.theta = target_theta + 180
        if abs(-robot.theta + target_theta) < (360 -robot.theta + target_theta) % 360:
            cmd.dtheta = -robot.theta + target_theta
        else:
            cmd.dtheta = (360 - robot.theta + target_theta) % 360

        #cmd.dtheta =  -robot.theta + target_theta
        return cmd
    
    def strikeBall(self, robot: ObjData, ball: ObjData, strike_target_pos: np.ndarray) -> LowCmd:
        vec_ball_to_target = strike_target_pos - np.array([ball.x, ball.y])
        
        drive_through_point = np.array([ball.x, ball.y]) + 0.1 * (vec_ball_to_target / np.linalg.norm(vec_ball_to_target))

        strike_theta = np.rad2deg(np.arctan2(vec_ball_to_target[1], vec_ball_to_target[0]) + 90)
        
        cmd = self.moveToPoint(robot, drive_through_point, strike_theta, obstacles=[])
        return cmd

    def _calculate_potential_field_vector(self, robot_pos: np.ndarray, robot_vel: np.ndarray, target_pos: np.ndarray, obstacles: list[Obstacle]) -> np.ndarray:
        #attractive_vector = (target_pos - robot_pos)
        #attractive_vector = self.ATTRACTIVE_GAIN * (attractive_vector / np.linalg.norm(attractive_vector))
        attractive_vector = self.ATTRACTIVE_GAIN * (target_pos - robot_pos)

        net_repulsive_vector = np.array([0.0, 0.0])
        for obs in obstacles:
            vec_to_robot = robot_pos - obs.pos
            dist_to_robot = np.linalg.norm(vec_to_robot)
            
            if dist_to_robot < self.REPULSION_RADIUS:
                repulsion_magnitude = self.REPULSIVE_GAIN * (1.0 / dist_to_robot - 1.0 / self.REPULSION_RADIUS)
                
                repulsive_force = repulsion_magnitude * (vec_to_robot / dist_to_robot)
                net_repulsive_vector += repulsive_force

        #damping_vector = -self.DAMPING_GAIN * robot_vel

        return attractive_vector + net_repulsive_vector

    def _world_to_robot_frame(self, vector: np.ndarray, robot_theta_deg: float) -> tuple[float, float]:
        theta_rad = np.deg2rad(robot_theta_deg)
        c, s = np.cos(theta_rad), np.sin(theta_rad)
        
        vx_world, vy_world = vector[0], vector[1]
        
        vx_robot = c * vx_world + s * vy_world
        vy_robot = -s * vx_world + c * vy_world
        
        return vx_robot, vy_robot
        
    def _cap_speed(self, vx: float, vy: float) -> tuple[float, float]:
        speed = np.sqrt(vx**2 + vy**2)
        if speed > self.MAX_LINEAR_SPEED:
            scale_factor = self.MAX_LINEAR_SPEED / speed
            return vx * scale_factor, vy * scale_factor
        return vx, vy

class Strat(Node):
    def __init__(self):
        super().__init__('strat')
        self.skills = SkillLib()
        
        self.field_subscriber = self.create_subscription(FieldData, 'field_data', self.gpCB, 10)
        
        self.cmd_publishers = {
            0: self.create_publisher(LowCmd, '/low0', 10),
            1: self.create_publisher(LowCmd, '/low1', 10),
            2: self.create_publisher(LowCmd, '/low2', 10)
        }
        
        self.get_logger().info("Strategist node initialized.")
        self.cmd = None
        self.timer = self.create_timer(0.1, self.send)

    def send(self):
        if self.cmd is not None:
            self.cmd_publishers[0].publish(self.cmd)

    def gpCB(self, field: FieldData):       
        target_coords = np.array([0, 0])
        target_angle = 0.0

        command = self.skills.moveToPoint(field.robot0, target_coords, target_angle, [])
        self.cmd = command
        #self.cmd_publishers[0].publish(command)
        
        """
        # Ejemplo 2: Mover el robot2 (evitando obstaculos) a la coordenada (3, -5) y que gire a 0°
        target_coords = np.array([3, -5])
        target_angle = 0.0

        # Todos los robots del campo
        all_robots = [field.robot0, field.robot1, field.robot2, field.robot3, field.robot4, field.robot5]
        obstacles = []
        for robot in all_robots:
            # Por cada robot (excepto el 0 que es el que estamos controlando), agregamos sus coordenadas como un obstaculo
            if robot != field.robot2:
                obstacle = Obstacle(robot.x, robot.y)
                obstacles.append(obstacle)

        # Llamamos moveToPoint() con la lista de obstaculos
        command = self.skills.moveToPoint(field.robot2, target_coords, target_angle, obstacles)

        # Comunicar el comando al robot2
        self.cmd_publishers[2].publish(command)
        """

        """
        # Ejemplo 3: Los ejemplos 1 y 2 juntos, ademas de que el robot1 sigue la pelota
        r0_target_coords = np.array([0, 0])
        r0_target_angle = 45.0
        r0_command = self.skills.moveToPoint(field.robot0, r0_target_coords, r0_target_angle, [])

        r2_target_coords = np.array([3, -5])
        r2_target_angle = 0.0
        all_robots = [field.robot0, field.robot1, field.robot2, field.robot3, field.robot4, field.robot5]
        obstacles = []
        for robot in all_robots:
            if robot != field.robot2:
                obstacle = Obstacle(robot.x, robot.y)
                obstacles.append(obstacle)
        r2_command = self.skills.moveToPoint(field.robot2, r2_target_coords, r2_target_angle, obstacles)

        # El objetivo es donde sea que este la pelota
        r1_target_coords = np.array([field.ball.x+1, field.ball.y])
        r1_target_angle = -90.0
        obstacles = []
        for robot in all_robots:
            if robot != field.robot1:
                obstacle = Obstacle(robot.x, robot.y)
                obstacles.append(obstacle)
        r1_command = self.skills.moveToPoint(field.robot1, r1_target_coords, r1_target_angle, obstacles)

        # Comunicar los comandos a los 3 robots
        self.cmd_publishers[0].publish(r0_command)
        self.cmd_publishers[1].publish(r1_command)
        self.cmd_publishers[2].publish(r2_command)
        """

        return

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