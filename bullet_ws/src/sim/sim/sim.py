import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
#from geometry_msgs.msg import Twist
from sim_msgs.msg import LowCmd, ObjData, FieldData
from sim_msgs.srv import Reset
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge
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

DT = 1./240.
DAMPING = 0
KP = 5
FRICTION = 0.6
MAX_FORCE = 5
MAX_TORQUE = 5
NUM_ROBOTS = 6
COLORS = {
    "red": [204/255, 0/255, 1/255],
    "green": [0/255, 204/255, 8/255],
    "blue": [5/255, 11/255, 159/255],
    "light_blue": [0/255, 170/255, 206/255],
    "yellow": [255/255, 230/255, 13/255],
    "purple": [205/255, 23/255, 220/255]
}

# x,y, theta, vx, vy (pelota primero)
DEFAULT_SETTINGS = [
    [0, 0, 0, 0, 0],
    [3, -3, 0, 0, 0,],
    [3, 0, 0, 0, 0],
    [3, 3, 0, 0, 0],
    [-3, -3, 0, 0, 0],
    [-3, 0, 0, 0, 0],
    [-3, 3, 0, 0, 0]
]

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
        combinations = [
            [main, p[0], p[1]] for p in secondary
        ]
        result.extend(random.sample(combinations, 3))
            
    return result

class Robot:
    def __init__(self, id, colors, initial_pos = [0, 0], initial_angle = 0):
        self.id = id
        self.initial_settings = initial_pos + [initial_angle, 0, 0, 0]
        self.src_lock = threading.Lock()
        self.tgt_lock = threading.Lock()
        self.curr_pos = [0, 0, 0]
        self.tgt = [0, 0, initial_angle]
        self.obj = p.loadURDF(os.path.join(get_package_share_directory('sim'), 'urdf', 'robot.urdf'), initial_pos, p.getQuaternionFromEuler([0, 0, math.radians(initial_angle)]))
        # ??????
        #p.changeDynamics(self.obj, 0, linearDamping = DAMPING, angularDamping = DAMPING)
        #p.changeDynamics(self.obj, 0, lateralFriction = FRICTION)
        p.changeVisualShape(self.obj, getJoint(self.obj, "main_color_joint"), rgbaColor = COLORS[colors[0]] + [1])
        p.changeVisualShape(self.obj, getJoint(self.obj, "secondary_color_joint1"), rgbaColor = COLORS[colors[1]] + [1])
        p.changeVisualShape(self.obj, getJoint(self.obj, "secondary_color_joint2"), rgbaColor = COLORS[colors[2]] + [1])

    def reset(self, settings):
        #self.initial_settings = settings
        with self.src_lock:
            self.curr_pos = [0, 0, 0]

        with self.tgt_lock:
            self.tgt = [0, 0, 0]

        p.resetBaseVelocity(self.obj, linearVelocity=[settings[3], settings[4], -1], angularVelocity=[0, 0, 0])
        p.resetBasePositionAndOrientation(self.obj, [settings[0], settings[1], 0.6], p.getQuaternionFromEuler([0, 0, math.radians(settings[2])]))

    def move(self, msg, local = False):
        with self.src_lock:
            curr_pos = self.curr_pos

        if local:
            # yikes
            #curr_pos[2] = msg[2]
            vx = msg[0] * math.cos(curr_pos[2]) - msg[1] * math.sin(curr_pos[2])
            vy = msg[0] * math.sin(curr_pos[2]) + msg[1] * math.cos(curr_pos[2])
            vel = [vx, vy, msg[2]]
        else:
            vel = msg

        with self.tgt_lock:
            self.tgt = vel
    
    def apply(self):
        with self.tgt_lock:
            tgt = self.tgt

        position, orientation = p.getBasePositionAndOrientation(self.obj)
        _, _, curr_angle = p.getEulerFromQuaternion(orientation)
        with self.src_lock:
            self.curr_pos = [position[0], position[1], curr_angle]

        #tgt_angle = math.radians(tgt[2])
        #error = tgt_angle - curr_anglex|
        error = -math.radians(tgt[2])
        error = math.atan2(math.sin(error), math.cos(error))
        correction = max(-MAX_TORQUE, min(MAX_TORQUE, KP * error))

        pos, orn = p.getBasePositionAndOrientation(self.obj)
        _, _, yaw = p.getEulerFromQuaternion(orn)
        new_orn = p.getQuaternionFromEuler([0, 0, yaw])
        p.resetBasePositionAndOrientation(self.obj, pos, new_orn)

        p.resetBaseVelocity(self.obj, linearVelocity=[tgt[0], tgt[1], -1], angularVelocity=[0, 0, correction])
        return

        linear, _ = p.getBaseVelocity(self.obj)
        angular = p.getJointState(self.obj, 0)[1] / (16*math.pi)
        #angular = p.getJointState(self.obj, 0)[1]
        curr_vel = np.array([linear[0], linear[1], angular])
        error = tgt_vel - curr_vel
        self.error_integral += error * DT
        error_derivative = (error - self.prev_error) / DT
        self.prev_error = error.copy()
        control_output = (self.kp * error + self.ki * self.error_integral +  self.kd * error_derivative)
        p.applyExternalForce(self.obj, 1, forceObj=[control_output[0], control_output[1], 0], posObj=[0, 0, 0], flags=p.WORLD_FRAME)
        p.applyExternalTorque(self.obj, 1, torqueObj=[0, 0, control_output[2]], flags=p.WORLD_FRAME)
        
        if self.id == 0:
            vel = p.getJointState(self.obj, 0)
            print(f"Joint0: {vel[1]}, error: {error}, output: {control_output}")
            """
            for j in range(p.getNumJoints(self.obj)):
                vel = p.getJointState(self.obj, j)
                print(f"Joint {j} velocity:", vel)    
            """    
        
class Camera:
    def __init__(self, res, fov = 60, target = [0, 0, 0]):
        self.target = target
        self.res = res
        self.fov = fov
    
    def cap(self):
        view_matrix = p.computeViewMatrixFromYawPitchRoll(
            cameraTargetPosition = self.target,
            distance = 12,
            yaw = 0,
            pitch = -90,
            roll = 0, 
            upAxisIndex = 2
        )
        proj_matrix = p.computeProjectionMatrixFOV(
            fov = self.fov,
            aspect = self.res[0] / self.res[1],
            nearVal = 0.1,
            farVal = 20.0
        )
        width, height, rgb, depth, seg = p.getCameraImage(
            width = self.res[0],
            height = self.res[1],
            viewMatrix = view_matrix,
            projectionMatrix = proj_matrix
        )
        frame = np.reshape(rgb, (height, width, 4))
        return cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

class Sim(Node):
    def __init__(self):
        super().__init__('sim')
        self.img_publisher = self.create_publisher(Image, 'sim_cam/image_raw', 10)
        self.cv_bridge = CvBridge()
        for i in range(NUM_ROBOTS):
            self.create_subscription(LowCmd, f'/low{i}', lambda msg, id=i: self.cmdCB(msg, id), 10)
            
        self.score1_publisher = self.create_publisher(Int32, 'score1', 10)
        self.score2_publisher = self.create_publisher(Int32, 'score2', 10)
        self.reset_service = self.create_service(Reset, 'sim/reset', self.resetCB)
        self.settings = DEFAULT_SETTINGS

        p.connect(p.GUI)
        p.setGravity(0, 0, -9.81)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.loadURDF(os.path.join(get_package_share_directory('sim'), 'urdf', 'field.urdf'), [0, 0, 0])
        self.score = [0, 0]
        self.ball = p.loadURDF(os.path.join(get_package_share_directory('sim'), 'urdf', 'ball.urdf'), [0, 0, 0.3])
        color_combinations = colorCombinations()
        self.robots = [Robot(i, color_combinations[i], DEFAULT_SETTINGS[i+1][:2] + [0.6], random.randint(0, 360)) for i in range(NUM_ROBOTS)]
        self.cam = Camera([480, 360])
        self.stop_event = threading.Event()
        self.sim_thread = threading.Thread(target = self.simStep)
        self.cap_thread = threading.Thread(target = self.camCap)
        self.sim_thread.start()
        self.cap_thread.start()

    def extractData(self, data):
        return [
            float(data.x),
            float(data.y), 
            float(data.theta),
            float(data.vx),
            float(data.vy),
            float(data.w)
        ]

    def resetCB(self, msg, response):
        print("EXTERNAL RESET CALLED")
        try:
            field_data = msg.settings
            obj_data = []
            
            ball_data = self.extractData(field_data.ball)
            if ball_data[0] == 999:
                self.reset()
                response.success = True  
                self.score = [0, 0]
                return response    

            obj_data.append(ball_data)
                        
            for i in range(6):
                robot = getattr(field_data, f'robot{i}')
                obj_data.append(self.extractData(robot))
                
            self.reset(obj_data)
            
            response.success = True       
        except Exception as e:
            print(f"Error: {str(e)}")
            response.success = False   

        self.score = [0, 0]

        return response

    def checkGoal(self):
        position, _ = p.getBasePositionAndOrientation(self.ball)
        if position[0] < -7.5:
            self.score[1] += 1
            print(f"GOAL ON LEFT, SCORE: {self.score}")
            msg = Int32()
            msg.data = self.score[1]
            self.score2_publisher.publish(msg)
            self.reset()
        elif position[0] > 7.5:
            self.score[0] += 1
            msg = Int32()
            msg.data = self.score[0]
            self.score1_publisher.publish(msg)
            print(f"GOAL ON RIGHT, SCORE: {self.score}")
            self.reset()

    def reset(self, settings = DEFAULT_SETTINGS):
        p.resetBaseVelocity(self.ball, linearVelocity = [settings[0][3], settings[0][4], -1], angularVelocity=[0, 0, 0])
        p.resetBasePositionAndOrientation(self.ball, [settings[0][0], settings[0][1], 0.6], p.getQuaternionFromEuler([0, 0, math.radians(settings[0][2])]))
        for i, robot in enumerate(self.robots):
            robot.reset(settings[i+1])

    def simStep(self):
        while not self.stop_event.is_set() and rclpy.ok():
            for robot in self.robots:
                robot.apply()

            p.stepSimulation()
            self.checkGoal()            
            time.sleep(DT)

    def cmdCB(self, msg: LowCmd, id: int):
        self.robots[id].move([msg.vx*2, msg.vy*2, msg.dtheta], msg.local)

    def msgCB(self, msg):
        str = msg.data
        if str == "reset":
            self.reset()

    def camCap(self):
        while not self.stop_event.is_set() and rclpy.ok():
            frame = self.cam.cap()
            msg = self.cv_bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.img_publisher.publish(msg)
            time.sleep(1./24.)

    def destroyNode(self):
        self.stop_event.set()
        self.sim_thread.join()
        self.cap_thread.join()
        p.disconnect()
        super().destroy_node()
            
def main(args=None):
    rclpy.init(args=args)
    node = Sim()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroyNode()
        rclpy.shutdown()

if __name__ == '__main__':
    main()