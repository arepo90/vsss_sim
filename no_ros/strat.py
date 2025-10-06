# gracias gemini por:
import numpy as np
import time
import socket
import pickle
import threading
import math

# ==============================================================================
# 1. COMMUNICATIONS LIBRARY (Replaces ROS2)
# ==============================================================================

# This port map must be IDENTICAL to the one in the other scripts.
TOPIC_PORTS = {
    'camera/image_raw': 10001,
    '/low0': 10002,
    '/low1': 10003,
    '/low2': 10004,
    'score1': 10005,
    'score2': 10006,
    'sim/controller': 10007,
    'field_data': 10008,
}

class UDPCommunicator:
    """A simple UDP-based communicator to replace ROS2 pub/sub and services."""
    def __init__(self):
        self.subscribers = {}
        self.threads = []
        self.running = True

    def publish(self, topic, data):
        """Serializes and sends data to a given topic's port."""
        if topic not in TOPIC_PORTS:
            print(f"Warning: Topic '{topic}' not in port map. Cannot publish.")
            return
        port = TOPIC_PORTS[topic]
        payload = pickle.dumps(data)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(payload, ('<broadcast>', port))

    def subscribe(self, topic, callback):
        """Starts a thread to listen for data on a topic's port."""
        if topic not in TOPIC_PORTS:
            print(f"Warning: Topic '{topic}' not in port map. Cannot subscribe.")
            return
        port = TOPIC_PORTS[topic]
        self.subscribers[port] = callback
        thread = threading.Thread(target=self._listen_topic, args=(port,), daemon=True)
        self.threads.append(thread)
        thread.start()

    def _listen_topic(self, port):
        """Listener loop for a single topic."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', port))
            while self.running:
                try:
                    payload, _ = s.recvfrom(65536)
                    data = pickle.loads(payload)
                    self.subscribers[port](data)
                except Exception as e:
                    print(f"Error while listening on port {port}: {e}")

    def shutdown(self):
        self.running = False

# ==============================================================================
# 2. MESSAGE DEFINITIONS (Replaces .msg files)
# ==============================================================================

class LowCmd:
    """Replicates sim_msgs/msg/LowCmd"""
    def __init__(self, robot_id=0, vx=0.0, vy=0.0, dtheta=0.0, local=False):
        self.robot_id, self.vx, self.vy, self.dtheta = robot_id, vx, vy, dtheta
        self.local = local # Assuming `local` is part of the msg for the sim

class ObjData:
    """Replicates sim_msgs/msg/ObjData"""
    def __init__(self, obj_id=0, current=False, x=0.0, y=0.0, theta=0.0, vx=0.0, vy=0.0, w=0.0):
        self.obj_id, self.current = obj_id, current
        self.x, self.y, self.theta = x, y, theta
        self.vx, self.vy, self.w = vx, vy, w

class FieldData:
    """Replicates sim_msgs/msg/FieldData"""
    def __init__(self):
        self.ball = ObjData()
        self.robot0, self.robot1, self.robot2 = ObjData(), ObjData(), ObjData()
        self.robot3, self.robot4, self.robot5 = ObjData(), ObjData(), ObjData()
        self.score1, self.score2 = 0, 0

# ==============================================================================
# 3. STRATEGY CORE LOGIC (Largely unchanged)
# ==============================================================================

FIELD_LENGTH = 17
MY_GOAL_POS = np.array([FIELD_LENGTH / 2, 0.0])
OPPONENT_GOAL_POS = np.array([-FIELD_LENGTH / 2, 0.0])

class Obstacle:
    def __init__(self, x, y, radius=0.4):
        self.pos = np.array([x, y])
        self.radius = radius

class SkillLib:
    def __init__(self):
        self.ATTRACTIVE_GAIN = 8        # que tanto quiere llegar al objetivo
        self.REPULSIVE_GAIN = 5         # que tanto quiere evitar obstaculos
        self.REPULSION_RADIUS = 5       # desde que tan lejos quiere evitar obstaculos
        self.MAX_LINEAR_SPEED = 3.0
        
    def moveToPoint(self, robot: ObjData, target_pos: np.ndarray, target_theta: float, obstacles: list[Obstacle]) -> LowCmd:
        robot_pos = np.array([robot.x, robot.y])
        robot_vel = np.array([robot.vx, robot.vy])

        vx_world, vy_world = self._calculate_potential_field_vector(robot_pos, robot_vel, target_pos, obstacles)
        
        vx_capped, vy_capped = self._cap_speed(vx_world, vy_world)

        cmd = LowCmd()
        cmd.robot_id = robot.obj_id
        cmd.vx = vx_capped
        cmd.vy = vy_capped
        cmd.dtheta = -robot.theta + target_theta
        cmd.local = False # Velocities are in world frame
        return cmd
    
    def _calculate_potential_field_vector(self, robot_pos: np.ndarray, robot_vel: np.ndarray, target_pos: np.ndarray, obstacles: list[Obstacle]) -> np.ndarray:
        attractive_vector = (target_pos - robot_pos)
        if np.linalg.norm(attractive_vector) > 0:
            attractive_vector = self.ATTRACTIVE_GAIN * (attractive_vector / np.linalg.norm(attractive_vector))

        net_repulsive_vector = np.array([0.0, 0.0])
        for obs in obstacles:
            vec_to_robot = robot_pos - obs.pos
            dist_to_robot = np.linalg.norm(vec_to_robot)
            
            if 0 < dist_to_robot < self.REPULSION_RADIUS:
                repulsion_magnitude = self.REPULSIVE_GAIN * (1.0 / dist_to_robot - 1.0 / self.REPULSION_RADIUS)
                repulsive_force = repulsion_magnitude * (vec_to_robot / dist_to_robot)
                net_repulsive_vector += repulsive_force

        return attractive_vector + net_repulsive_vector
        
    def _cap_speed(self, vx: float, vy: float) -> tuple[float, float]:
        speed = np.sqrt(vx**2 + vy**2)
        if speed > self.MAX_LINEAR_SPEED:
            scale_factor = self.MAX_LINEAR_SPEED / speed
            return vx * scale_factor, vy * scale_factor
        return vx, vy

class Strat:
    def __init__(self):
        self.skills = SkillLib()
        self.comms = UDPCommunicator()
        
        # Subscribe to field data from the vision script
        self.comms.subscribe('field_data', self.gpCB)
        
        print("Strategist node initialized and listening for field data.")

    def gpCB(self, field: FieldData):  
        # Aqui va el programa general:

        """
        # Ejemplo 1: Mover el robot0 (en linea recta) a la coordenada (0, 0) y que se oriente a 45°
        target_coords = np.array([0, 0])
        target_angle = 45.0

        # Para usar moveToPoint(), hay que darle de argumentos el robot a mover (robot0), el objetivo (target_coords, target_angle),
        # y la lista de obstaculos (en este caso nada, entonces solo se movera en linea recta)
        command = self.skills.moveToPoint(field.robot0, target_coords, target_angle, [])

        # Comunicar el comando al robot0
        self.comms.publish('/low0', command)
        """

        """
        # Ejemplo 2: Mover el robot2 (evitando obstaculos) a la coordenada (3, -5) y que se oriente a 0°
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
        self.comms.publish('/low2', command)
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

        # El objetivo es donde sea que este la pelota, pero ligeramente atras
        r1_target_coords = np.array([field.ball.x+1, field.ball.y])
        r1_target_angle = -90.0
        obstacles = []
        for robot in all_robots:
            if robot != field.robot1:
                obstacle = Obstacle(robot.x, robot.y)
                obstacles.append(obstacle)
        r1_command = self.skills.moveToPoint(field.robot1, r1_target_coords, r1_target_angle, obstacles)

        self.comms.publish('/low0', r0_command)
        self.comms.publish('/low1', r1_command)
        self.comms.publish('/low2', r2_command)
        """

    def shutdown(self):
        self.comms.shutdown()
        print("Strategy node shut down.")

# ==============================================================================
# 4. MAIN EXECUTION BLOCK
# ==============================================================================
def main():
    node = Strat()
    try:
        # Keep the main thread alive, the comms thread is a daemon
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt caught, shutting down.")
    finally:
        node.shutdown()

if __name__ == '__main__':
    main()