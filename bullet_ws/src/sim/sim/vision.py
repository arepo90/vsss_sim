import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from sim_msgs.msg import FieldData, ObjData, Settings
from std_msgs.msg import Int32, Int32MultiArray
import cv2
import numpy as np
import math
import os
import glob
import time
import threading


def openCamera(logger=None):
    devices = sorted(glob.glob('/dev/video*'))
    for dev in devices:
        if dev == '/dev/video0':
            continue
        try:
            idx = int(dev.replace('/dev/video', ''))
        except ValueError:
            continue
        cap = cv2.VideoCapture(idx, cv2.CAP_V4L2)
        if cap.isOpened():
            if logger is not None:
                logger.info(f"Opened {dev}")
            return cap
        cap.release()
    return None

USE_LOCAL = True
CAM_EXPOSURE = 400
TEAM_COLOR = "yellow"
OP_COLOR = "blue"

MIN_AREA = 40

ORANGE_RANGE = [(2, 100, 100), (20, 255, 255)]

OBJ_LABELS = ["Ball", "yellow0", "yellow1", "yellow2", "blue0", "blue1", "blue2"]
DETECTION_TIMEOUT = 5

BLUE_IDS = {256: 0, 272: 1, 273: 2}
YELLOW_IDS = {955: 0, 771: 1, 939: 2}

try:
    ARUCO_DICT = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
    ARUCO_PARAMS = cv2.aruco.DetectorParameters()
    ARUCO_DETECTOR = cv2.aruco.ArucoDetector(ARUCO_DICT, ARUCO_PARAMS)
    def _detect_aruco(gray):
        return ARUCO_DETECTOR.detectMarkers(gray)
except AttributeError:
    ARUCO_DICT = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    ARUCO_PARAMS = cv2.aruco.DetectorParameters_create()
    def _detect_aruco(gray):
        return cv2.aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMS)


class Detector:
    def reset(self):
        pass

    def detectBall(self, img):
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, ORANGE_RANGE[0], ORANGE_RANGE[1])
        kernel = np.ones((2, 2), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        filtered = [c for c in contours if cv2.contourArea(c) > MIN_AREA]
        if not filtered:
            return [999, 999, 999]

        sorted_contours = sorted(filtered, key=cv2.contourArea, reverse=True)
        TOLERANCE = 0.1
        best_ratio = 999
        best_obs = None
        for cont in sorted_contours[:3]:
            if len(cont) < 5:
                continue
            (x, y), (major, minor), _ = cv2.fitEllipse(cont)
            ellipse_area = np.pi * (major / 2) * (minor / 2)
            ratio = ellipse_area / cv2.contourArea(cont)
            if 1.0 - TOLERANCE < ratio < 1.0 + TOLERANCE and ratio < best_ratio:
                best_ratio = ratio
                best_obs = [float(x), float(y), 0.0]

        if best_obs is None:
            return [999, 999, 999]
        return best_obs

    def detectMarkers(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = _detect_aruco(gray)
        out = {}
        if ids is None:
            return out
        for i, mid in enumerate(ids.flatten()):
            mid = int(mid)
            if mid in YELLOW_IDS:
                label = f"yellow{YELLOW_IDS[mid]}"
            elif mid in BLUE_IDS:
                label = f"blue{BLUE_IDS[mid]}"
            else:
                continue
            c = corners[i][0]
            cx = float(np.mean(c[:, 0]))
            cy = float(np.mean(c[:, 1]))
            dx = float(c[1, 0] - c[0, 0])
            dy = float(c[1, 1] - c[0, 1])
            angle = (math.degrees(math.atan2(dy, dx)) + 360.0) % 360.0
            out[label] = [cx, cy, angle]
        return out


class Kalman:
    def __init__(self, id):
        self.id = id

        self.x = np.zeros((6, 1))
        self.P = np.eye(6) * 1.0

        self.H = np.array([
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0]
        ])

        Q_diag = [3e-5, 3e-5, 1e-5, 0.06, 0.06, 0.1]
        R_diag = [4e-3, 4e-3, 1e-3]

        self.Q = np.diag(Q_diag)
        self.R = np.diag(R_diag)

        self.I = np.eye(6)

        self.field_width_m = 17
        self.field_height_m = 13

    def reset(self):
        self.x = np.zeros((6, 1))
        self.P = np.eye(6) * 1.0

    def predict(self, dt):
        F = np.eye(6)
        F[0, 3] = dt
        F[1, 4] = dt
        F[2, 5] = dt

        self.x = F @ self.x
        self.P = F @ self.P @ F.T + self.Q
        return self.x.flatten()

    def update(self, z_raw, px_dims):
        x_px, y_px, angle_deg = z_raw
        scale_x = self.field_width_m / px_dims[0]
        scale_y = self.field_height_m / px_dims[1]
        x_m = (x_px - px_dims[0] / 2.0) * scale_x
        y_m = (px_dims[1] / 2.0 - y_px) * scale_y

        angle_rad_raw = math.radians(angle_deg)
        angle_rad = np.arctan2(np.sin(angle_rad_raw), np.cos(angle_rad_raw))

        z = np.array([[x_m], [y_m], [angle_rad]])

        y = z - self.H @ self.x
        y[2] = (y[2] + np.pi) % (2 * np.pi) - np.pi

        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.x = self.x + K @ y
        self.P = (self.I - K @ self.H) @ self.P

        return self.x.flatten()

    def getState(self):
        return {
            "x": float(self.x[0]),
            "y": float(self.x[1]),
            "theta": float(self.x[2]),
            "vx": float(self.x[3]),
            "vy": float(self.x[4]),
            "w": float(self.x[5]),
        }


class Vision(Node):
    def __init__(self):
        super().__init__('vision')
        #os.close(2); os.open(os.devnull, os.O_WRONLY)
        self.publisher = self.create_publisher(FieldData, 'field_data', 10)
        self.detector = Detector()
        self.kalman = [Kalman(i) for i in range(7)]
        self.is_calibrated = False
        self.prev = time.time()
        self.src_list = []
        self.dst_list = []
        self.active = [0, 0, 0]
        self.mapping = [-1, -1, -1]
        self.settings_subscriber = self.create_subscription(Settings, 'settings', self.settingsCB, 10)
        self.active_subscriber = self.create_subscription(Int32MultiArray, 'active', self.activeCB, 10)
        self.is_running = threading.Event()
        self.is_local = threading.Event()
        self.video_publisher = self.create_publisher(Image, 'local_cam/image_raw', 10)
        self.video_subscriber = self.create_subscription(Image, 'sim_cam/image_raw', self.visionCB, 10)
        self.cv_bridge = CvBridge()
        self.seen = [0 for _ in range(7)]
        self.reset_pattern = True
        self.counter = 0
        self.cam_thread = threading.Thread(target=self.visionTCB)
        if USE_LOCAL:
            self.cam = openCamera(self.get_logger())
            if self.cam is None:
                self.get_logger().error("Failed to open camera")
                return

            self.camSetup()
            self.cam_thread.start()
        else:
            self.is_local.set()

    def activeCB(self, msg):
        for i in range(3):
            if self.mapping[i] != -1:
                self.active[self.mapping[i]] = msg.data[self.mapping[i]]

    def settingsCB(self, msg):
        global CAM_EXPOSURE, USE_LOCAL, TEAM_COLOR, OP_COLOR
        if msg.local and not USE_LOCAL:
            self.get_logger().info("Switched to local")
            USE_LOCAL = True
            self.is_local.clear()
            self.cam = openCamera(self.get_logger())
            if self.cam is None:
                self.get_logger().error("Failed to open camera")
                return

            self.camSetup()
            self.cam_thread = threading.Thread(target=self.visionTCB)
            self.cam_thread.start()
        elif not msg.local and USE_LOCAL:
            self.get_logger().info("Switched to sim")
            USE_LOCAL = False
            self.is_local.set()
            if self.cam_thread.is_alive():
                self.cam_thread.join()

            if self.cam.isOpened():
                self.cam.release()

        self.mapping = [msg.robot0, msg.robot1, msg.robot2]

        if TEAM_COLOR != ("yellow" if msg.team_color else "blue"):
            TEAM_COLOR = "yellow" if msg.team_color else "blue"
            OP_COLOR = "blue" if msg.team_color else "yellow"

        if USE_LOCAL and msg.exposure != CAM_EXPOSURE:
            CAM_EXPOSURE = msg.exposure
            self.cam.set(cv2.CAP_PROP_EXPOSURE, CAM_EXPOSURE)

        if msg.reset != self.reset_pattern:
            self.reset_pattern = msg.reset
            self.seen = [0 for _ in range(7)]
            for k in self.kalman:
                k.reset()

            self.detector.reset()

    def camSetup(self):
        global CAM_EXPOSURE
        self.cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        self.cam.set(cv2.CAP_PROP_EXPOSURE, CAM_EXPOSURE)

    def visionProc(self, img):
        if img is None:
            self.get_logger().warning("Bad image")
            return None

        if not self.is_calibrated:
            cv2.namedWindow('src')
            cv2.namedWindow('dst')
            cv2.setMouseCallback('src', self.srcCB)
            cv2.setMouseCallback('dst', self.dstCB)
            self.is_calibrated = self.calibrate(img.copy(), True)
            cv2.destroyWindow('src')
            cv2.destroyWindow('dst')

        norm = cv2.warpPerspective(img, self.H, (img.shape[1], img.shape[0]))
        norm = norm[40:700, 50:1255]

        ball = self.detector.detectBall(norm)
        markers = self.detector.detectMarkers(norm)

        accumulated = {label: [999, 999, 999] for label in OBJ_LABELS}
        accumulated["Ball"] = ball
        for label, obs in markers.items():
            accumulated[label] = obs

        observation = [accumulated[label] for label in OBJ_LABELS]
        states = []
        curr = time.time()
        dt = curr - self.prev
        for i, obs in enumerate(observation):
            self.kalman[i].predict(dt)
            if obs[0] != 999:
                self.kalman[i].update(obs, [norm.shape[1], norm.shape[0]])
                self.seen[i] = time.time()

            if time.time() - self.seen[i] < DETECTION_TIMEOUT:
                states.append(self.kalman[i].getState())
            else:
                states.append({
                    "x": 999.,
                    "y": 999.,
                    "theta": 999.,
                    "vx": 999.,
                    "vy": 999.,
                    "w": 999.,
                })

        self.prev = curr
        field_data = self.getMsg(states)
        self.publisher.publish(field_data)
        return norm

    def visionTCB(self):
        while rclpy.ok() and not self.is_running.is_set() and not self.is_local.is_set():
            _, img = self.cam.read()
            if self.counter < 10:
                self.counter += 1
                cv2.waitKey(1)
                continue

            if img is None:
                continue

            last = self.visionProc(img)
            if last is None:
                continue

            msg = self.cv_bridge.cv2_to_imgmsg(last, encoding="bgr8")
            self.video_publisher.publish(msg)
            cv2.waitKey(1)

    def visionCB(self, msg: Image):
        if not self.is_local.is_set():
            return

        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        last = self.visionProc(img)
        if last is None:
            return

        msg = self.cv_bridge.cv2_to_imgmsg(last, encoding="bgr8")
        self.video_publisher.publish(msg)
        cv2.waitKey(1)

    def getMsg(self, data):
        msg = FieldData()
        msg.ball = ObjData(
            obj_id=0,
            current=True,
            x=data[0]["x"],
            y=data[0]["y"],
            theta=(math.degrees(data[0]["theta"]) + 90) % 360,
            vx=data[0]["vx"],
            vy=data[0]["vy"],
            w=data[0]["w"]
        )

        global TEAM_COLOR
        if TEAM_COLOR == "blue":
            order = [0, 4, 5, 6, 1, 2, 3]
        else:
            order = list(range(len(OBJ_LABELS)))

        for msg_index, i in enumerate(order[1:], start=1):
            robot = ObjData(
                obj_id=i,
                current=True,
                x=data[i]["x"],
                y=data[i]["y"],
                theta=(math.degrees(data[i]["theta"]) + 90) % 360,
                vx=data[i]["vx"],
                vy=data[i]["vy"],
                w=data[i]["w"]
            )
            setattr(msg, f'{"team" if msg_index < 4 else "op"}{(msg_index-1) % 3}', robot)

        return msg

    def srcCB(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.src_x, self.src_y = x, y
            cv2.circle(self.src, (x, y), 5, (0, 0, 255), -1)

    def dstCB(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.dst_x, self.dst_y = x, y
            cv2.circle(self.dst, (x, y), 5, (0, 0, 255), -1)

    def calibrate(self, src, bypass=False):
        if bypass:
            if USE_LOCAL:
                self.H = np.array([
                    [1.34296942e+00, -4.24803062e-02, -3.71164632e+02],
                    [-1.17567175e-02, 9.31332598e-01, 2.23477780e+01],
                    [-7.21411831e-05, -4.25708252e-05, 1.00000000e+00]
                ])
            else:
                self.H = np.array([
                    [1.02222994e+00, -6.07657129e-03, -2.02668347e+00],
                    [-3.42416353e-03, 9.30203586e-01, 1.68165116e+01],
                    [1.11241564e-05, -3.17810579e-05, 1.00000000e+00]
                ])
            return True

        self.src = src
        self.dst = cv2.imread(os.path.join(get_package_share_directory('sim'), 'imgs', 'dst.png'))
        self.dst = cv2.resize(self.dst, (self.src.shape[1], self.src.shape[0]))
        self.get_logger().info("S - Save pair\nH - End")
        while True:
            cv2.imshow('src', self.src)
            cv2.imshow('dst', self.dst)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                self.get_logger().info('Pair saved')
                cv2.circle(self.src, (self.src_x, self.src_y), 5, (0, 255, 0), -1)
                cv2.circle(self.dst, (self.dst_x, self.dst_y), 5, (0, 255, 0), -1)
                self.src_list.append([self.src_x, self.src_y])
                self.dst_list.append([self.dst_x, self.dst_y])
            elif k == ord('h'):
                src_pts = np.array(self.src_list).reshape(-1, 1, 2)
                dst_pts = np.array(self.dst_list).reshape(-1, 1, 2)
                H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5)
                self.H = H
                print("H:", H)
                break
            elif k == ord('q'):
                self.H = np.array([
                    [1.02222994e+00, -6.07657129e-03, -2.02668347e+00],
                    [-3.42416353e-03, 9.30203586e-01, 1.68165116e+01],
                    [1.11241564e-05, -3.17810579e-05, 1.00000000e+00]
                ])
                break
            elif k == 27:
                return False

        return True

    def destroyNode(self):
        self.is_running.set()
        if USE_LOCAL:
            if self.cam_thread.is_alive():
                self.cam_thread.join()
            self.cam.release()

        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = Vision()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroyNode()
        rclpy.shutdown()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
