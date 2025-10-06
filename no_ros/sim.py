import pybullet as p
import pybullet_data
import time
import os
import threading
import cv2
import numpy as np
import itertools
import random
import math
import socket
import pickle

# ==============================================================================
# 1. COMMUNICATIONS LIBRARY (Replaces ROS2)
# ==============================================================================

# A simple mapping of topic/service names to ports.
# This would be in a shared config file in a real multi-program setup.
TOPIC_PORTS = {
    'camera/image_raw': 10001,
    '/low0': 10002,
    '/low1': 10003,
    '/low2': 10004,
    'score1': 10005,
    'score2': 10006,
    'sim/controller': 10007, # Service port
}

class UDPCommunicator:
    """A simple UDP-based communicator to replace ROS2 pub/sub and services."""
    def __init__(self):
        self.subscribers = {}
        self.service_callbacks = {}
        self.threads = []
        self.running = True

    def publish(self, topic, data):
        """Serializes and sends data to a given topic's port."""
        if topic not in TOPIC_PORTS:
            print(f"Warning: Topic '{topic}' not in port map. Cannot publish.")
            return
        
        port = TOPIC_PORTS[topic]
        
        # For images, compress to JPEG before sending to reduce size
        if isinstance(data, np.ndarray):
            _, buffer = cv2.imencode('.jpg', data, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            payload = pickle.dumps(('image', buffer))
        else:
            payload = pickle.dumps(data)

        # Broadcast on localhost
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

    def create_service(self, service_name, callback):
        """Starts a thread to listen for service requests and send responses."""
        if service_name not in TOPIC_PORTS:
            print(f"Warning: Service '{service_name}' not in port map. Cannot create.")
            return

        port = TOPIC_PORTS[service_name]
        self.service_callbacks[port] = callback

        thread = threading.Thread(target=self._listen_service, args=(port,), daemon=True)
        self.threads.append(thread)
        thread.start()

    def _listen_topic(self, port):
        """Listener loop for a single topic."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', port))
            while self.running:
                try:
                    payload, _ = s.recvfrom(65536) # Max UDP packet size
                    data = pickle.loads(payload)
                    
                    # Handle compressed images
                    if isinstance(data, tuple) and data[0] == 'image':
                        buffer = data[1]
                        img = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
                        self.subscribers[port](img)
                    else:
                        self.subscribers[port](data)
                except Exception as e:
                    print(f"Error while listening on port {port}: {e}")

    def _listen_service(self, port):
        """Listener loop for a service."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', port))
            while self.running:
                try:
                    payload, addr = s.recvfrom(65536)
                    request_data = pickle.loads(payload)
                    
                    # Call the service handler
                    callback = self.service_callbacks.get(port)
                    if callback:
                        response_data = callback(request_data)
                        response_payload = pickle.dumps(response_data)
                        s.sendto(response_payload, addr) # Send response back
                except Exception as e:
                    print(f"Error handling service on port {port}: {e}")

    def shutdown(self):
        """Stops the listener threads."""
        self.running = False
        print("Communications shutting down.")

# ==============================================================================
# 2. MESSAGE DEFINITIONS (Replaces .msg and .srv files)
# ==============================================================================

class LowCmd:
    """Replicates sim_msgs/msg/LowCmd"""
    def __init__(self, vx=0.0, vy=0.0, dtheta=0.0, local=False):
        self.vx = vx
        self.vy = vy
        self.dtheta = dtheta
        self.local = local

class ObjData:
    """Replicates sim_msgs/msg/ObjData"""
    def __init__(self, x=0.0, y=0.0, theta=0.0, vx=0.0, vy=0.0, w=0.0):
        self.x, self.y, self.theta = x, y, theta
        self.vx, self.vy, self.w = vx, vy, w

class FieldData:
    def __init__(self):
        self.ball = ObjData()
        self.robot0 = ObjData()
        self.robot1 = ObjData()
        self.robot2 = ObjData()
        self.robot3 = ObjData()
        self.robot4 = ObjData()
        self.robot5 = ObjData()

# --- Constants and Helpers (Unchanged) ---
DT = 1./240.
DAMPING = 0
KP = 5
FRICTION = 0.6
MAX_FORCE = 5
MAX_TORQUE = 5
NUM_ROBOTS = 3
COLORS = {
    "red": [204/255, 0/255, 1/255, 1], "green": [0/255, 204/255, 8/255, 1],
    "blue": [5/255, 11/255, 159/255, 1], "light_blue": [0/255, 170/255, 206/255, 1],
    "yellow": [255/255, 230/255, 13/255, 1], "purple": [205/255, 23/255, 220/255, 1]
}
DEFAULT_SETTINGS = [
    [0, 0, 0, 0, 0], [3, -3, 0, 0, 0], [3, 0, 0, 0, 0], [3, 3, 0, 0, 0],
    [-3, -3, 0, 0, 0], [-3, 0, 0, 0, 0], [-3, 3, 0, 0, 0]
]

def get_urdf_path(filename):
    script_dir = os.path.dirname(__file__)
    print(os.path.join(script_dir, 'urdf', filename))
    return os.path.join(script_dir, 'urdf', filename)

def getJoint(obj_id, joint_name: str) -> int:
    num_joints = p.getNumJoints(obj_id)
    for i in range(num_joints):
        info = p.getJointInfo(obj_id, i)
        if info[1].decode("utf-8") == joint_name:
            return i
    raise ValueError(f"Joint '{joint_name}' not found in body {obj_id}")

def colorCombinations():
    main_colors = ["blue", "yellow"]
    result = []
    for main in main_colors:
        options = [c for c in COLORS.keys() if c != "blue" and c != "yellow"]
        secondary = itertools.combinations(options, 2)
        combinations = [[main, p[0], p[1]] for p in secondary]
        result.extend(random.sample(combinations, 3))
    return result

# --- Class Definitions (Robot, Camera are unchanged) ---
class Robot:
    def __init__(self, id, colors, initial_pos = [0, 0], initial_angle = 0):
        self.id = id
        self.initial_settings = initial_pos + [initial_angle, 0, 0, 0]
        self.src_lock = threading.Lock()
        self.tgt_lock = threading.Lock()
        self.curr_pos = [0, 0, 0]
        self.tgt = [0, 0, initial_angle]
        self.obj = p.loadURDF(get_urdf_path('robot.urdf'), initial_pos, p.getQuaternionFromEuler([0, 0, math.radians(initial_angle)]))
        #self.obj = p.loadURDF('robot.urdf', initial_pos, p.getQuaternionFromEuler([0, 0, math.radians(initial_angle)]))
        p.changeVisualShape(self.obj, getJoint(self.obj, "main_color_joint"), rgbaColor=COLORS[colors[0]])
        p.changeVisualShape(self.obj, getJoint(self.obj, "secondary_color_joint1"), rgbaColor=COLORS[colors[1]])
        p.changeVisualShape(self.obj, getJoint(self.obj, "secondary_color_joint2"), rgbaColor=COLORS[colors[2]])

    def reset(self, settings):
        with self.src_lock: self.curr_pos = [0, 0, 0]
        with self.tgt_lock: self.tgt = [0, 0, 0]
        p.resetBaseVelocity(self.obj, linearVelocity=[settings[3], settings[4], -1], angularVelocity=[0, 0, 0])
        p.resetBasePositionAndOrientation(self.obj, [settings[0], settings[1], 0.6], p.getQuaternionFromEuler([0, 0, math.radians(settings[2])]))

    def move(self, msg, local = False):
        with self.src_lock: curr_pos = self.curr_pos
        if local:
            vx = msg[0] * math.cos(curr_pos[2]) - msg[1] * math.sin(curr_pos[2])
            vy = msg[0] * math.sin(curr_pos[2]) + msg[1] * math.cos(curr_pos[2])
            vel = [vx, vy, msg[2]]
        else:
            vel = msg
        with self.tgt_lock: self.tgt = vel
    
    def apply(self):
        with self.tgt_lock: tgt = self.tgt
        position, orientation = p.getBasePositionAndOrientation(self.obj)
        _, _, curr_angle = p.getEulerFromQuaternion(orientation)
        with self.src_lock: self.curr_pos = [position[0], position[1], curr_angle]
        error = -math.radians(tgt[2])
        error = math.atan2(math.sin(error), math.cos(error))
        correction = max(-MAX_TORQUE, min(MAX_TORQUE, KP * error))
        pos, orn = p.getBasePositionAndOrientation(self.obj)
        _, _, yaw = p.getEulerFromQuaternion(orn)
        new_orn = p.getQuaternionFromEuler([0, 0, yaw])
        p.resetBasePositionAndOrientation(self.obj, pos, new_orn)
        p.resetBaseVelocity(self.obj, linearVelocity=[tgt[0], tgt[1], -1], angularVelocity=[0, 0, correction])

class Camera:
    def __init__(self, res, fov = 60, target = [0, 0, 0]):
        self.target, self.res, self.fov = target, res, fov
    
    def cap(self):
        view_matrix = p.computeViewMatrixFromYawPitchRoll(cameraTargetPosition=self.target, distance=12, yaw=0, pitch=-90, roll=0, upAxisIndex=2)
        proj_matrix = p.computeProjectionMatrixFOV(fov=self.fov, aspect=self.res[0]/self.res[1], nearVal=0.1, farVal=20.0)
        width, height, rgb, _, _ = p.getCameraImage(width=self.res[0], height=self.res[1], viewMatrix=view_matrix, projectionMatrix=proj_matrix)
        frame = np.reshape(rgb, (height, width, 4))
        return cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

# --- Main Sim Class (Modified for new communication) ---
class Sim:
    def __init__(self):
        print("Initializing Simulation...")
        # Initialize communication
        self.comms = UDPCommunicator()

        # Set up subscriptions (replaces create_subscription)
        for i in range(NUM_ROBOTS):
            self.comms.subscribe(f'/low{i}', lambda msg, id=i: self.cmdCB(msg, id))
        
        # Set up services (replaces create_service)
        self.comms.create_service('sim/controller', self.resetCB)

        self.settings = DEFAULT_SETTINGS

        # PyBullet Setup
        p.connect(p.GUI)
        p.setGravity(0, 0, -9.81)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.loadURDF(get_urdf_path('field.urdf'), [0, 0, 0])
        #p.loadURDF('field.urdf', [0, 0, 0])
        self.score = [0, 0]
        self.ball = p.loadURDF(get_urdf_path('ball.urdf'), [0, 0, 0.3])
        #self.ball = p.loadURDF('ball.urdf', [0, 0, 0.3])
        color_combinations = colorCombinations()
        self.robots = [Robot(i, color_combinations[i], DEFAULT_SETTINGS[i+1][:2] + [0.6], 0) for i in range(NUM_ROBOTS)]
        self.cam = Camera([480, 360])
        
        # Threading Setup
        self.stop_event = threading.Event()
        self.sim_thread = threading.Thread(target=self.simStep)
        self.cap_thread = threading.Thread(target=self.camCap)
        self.sim_thread.start()
        self.cap_thread.start()
        print("Simulation running.")

    def extractData(self, data):
        return [data.x, data.y, data.theta, data.vx, data.vy, data.w]

    def resetCB(self, request_data):
        """Service callback. Receives request data, returns response data."""
        print("EXTERNAL RESET CALLED")
        response = {'success': False} # Default response
        try:
            field_data = request_data['settings']
            ball_data = self.extractData(field_data.ball)
            
            if ball_data[0] == 999: # Special value for default reset
                self.reset()
                self.score = [0, 0]
                response['success'] = True
                return response

            obj_data = [ball_data]
            for i in range(6):
                robot = getattr(field_data, f'robot{i}')
                obj_data.append(self.extractData(robot))
            
            self.reset(obj_data)
            self.score = [0, 0]
            response['success'] = True
        except Exception as e:
            print(f"Error in resetCB: {str(e)}")
            response['success'] = False
        return response

    def checkGoal(self):
        position, _ = p.getBasePositionAndOrientation(self.ball)
        if position[0] < -7.5:
            self.score[1] += 1
            print(f"GOAL ON LEFT, SCORE: {self.score}")
            self.comms.publish('score2', self.score[1])
            self.reset()
        elif position[0] > 7.5:
            self.score[0] += 1
            print(f"GOAL ON RIGHT, SCORE: {self.score}")
            self.comms.publish('score1', self.score[0])
            self.reset()

    def reset(self, settings = DEFAULT_SETTINGS):
        p.resetBaseVelocity(self.ball, linearVelocity=[settings[0][3], settings[0][4], -1], angularVelocity=[0, 0, 0])
        p.resetBasePositionAndOrientation(self.ball, [settings[0][0], settings[0][1], 0.6], p.getQuaternionFromEuler([0, 0, math.radians(settings[0][2])]))
        for i, robot in enumerate(self.robots):
            robot.reset(settings[i+1])

    def simStep(self):
        while not self.stop_event.is_set():
            for robot in self.robots:
                robot.apply()
            p.stepSimulation()
            self.checkGoal()            
            time.sleep(DT)

    def cmdCB(self, msg: LowCmd, id: int):
        self.robots[id].move([msg.vx, msg.vy, msg.dtheta], msg.local)

    def camCap(self):
        while not self.stop_event.is_set():
            frame = self.cam.cap()
            self.comms.publish('camera/image_raw', frame)
            time.sleep(1./24.)

    def destroyNode(self):
        print("Destroying node...")
        self.stop_event.set()
        if self.sim_thread.is_alive(): self.sim_thread.join()
        if self.cap_thread.is_alive(): self.cap_thread.join()
        self.comms.shutdown()
        p.disconnect()
        print("Node destroyed.")

# ==============================================================================
# 4. MAIN EXECUTION BLOCK
# ==============================================================================
def main():
    sim_node = Sim()
    try:
        # Keep the main thread alive, allowing background threads to run
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt caught, shutting down.")
    finally:
        sim_node.destroyNode()

if __name__ == '__main__':
    main()