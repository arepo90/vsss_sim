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
from itertools import combinations
import os
import time
import threading
import torch
from ultralytics import YOLO

counter = 0

USE_LOCAL = True
CAM_EXPOSURE = 400
TEAM_COLOR = "yellow"
OP_COLOR = "blue"

MIN_AREA = 40
SEARCH_RADIUS = 40
PATTERN_TOLERANCE = 0.5

"""
COLOR_RANGES = {
    "red": [(0, 125, 125), (12, 255, 255), (175, 100, 100), (0, 255, 255)],
    "orange": [(0, 200, 0), (10, 255, 255)],
    "yellow": [(0, 62, 220), (27, 145, 255)],
    "green": [(0, 50, 215), (45, 85, 255)],
    "light_blue": [(90, 95, 0), (102, 255, 255)],
    "blue": [(105, 50, 50), (130, 255, 255)], # missing
    "purple": [(161, 150, 0), (172, 255, 255)]
}
"""
COLOR_RANGES = {
    "red": [(0, 100, 100), (7, 255, 255), (170, 100, 100), (180, 255, 255)],
    "orange": [(2, 100, 100), (20, 255, 255)],
    "yellow": [(22, 25, 25), (30, 255, 255)],
    "green": [(35, 50, 50), (90, 255, 255)],
    "light_blue": [(90, 100, 100), (100, 255, 255)],
    "blue": [(101, 50, 50), (120, 255, 255)], 
    "purple": [(130, 50, 50), (167, 255, 255)]
}


OBJ_LABELS = ["Ball", "yellow0", "yellow1", "yellow2", "blue0", "blue1", "blue2"]
DETECTION_TIMEOUT = 5

def bisectorAngle(P, A, B):
    P = np.array(P, dtype=float)
    u = np.array(A, dtype=float) - P
    v = np.array(B, dtype=float) - P
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    if nu == 0 or nv == 0:
        raise ValueError("Vertex equals one of the other points")
    
    u /= nu
    v /= nv
    w = u + v
    nw = np.linalg.norm(w)
    if nw == 0:
        w = np.array([-u[1], u[0]])

    return (math.degrees(math.atan2(w[1], w[0])) + 360) % 360

def trisectorAngle(P, A, B, C):
    P = np.array(P, dtype=float)
    u = np.array(A, dtype=float)
    v = np.array(B, dtype=float)
    w = np.array(C, dtype=float)
    nu = np.linalg.norm(u)
    nv = np.linalg.norm(v)
    nw = np.linalg.norm(w)
    if nu == 0 or nv == 0 or nw == 0:
        return -1
    
    return np.degrees(np.atan2(w[1], w[0]) + 360) % 360

def centroid(A, B, C):
    x = (A[0] + B[0] + C[0]) // 3
    y = (A[1] + B[1] + C[1]) // 3
    return (x, y)

class PatternRegistry:
    def __init__(self):
        self.patterns = {}
        self.next_yellow = 0
        self.next_blue = 0

    def reset(self):
        self.patterns = {}
        self.next_yellow = 0
        self.next_blue = 0

    def detectBall(self, img):
        frame = img.copy()
        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, COLOR_RANGES["orange"][0], COLOR_RANGES["orange"][1])
        kernel = np.ones((2, 2), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        #cv2.imshow("mask", mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        filtered_contours = [cont for cont in contours if cv2.contourArea(cont) > MIN_AREA]
        if len(filtered_contours) == 0:
            return [999, 999, 999]
        
        sorted_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)

        TOLERANCE = 0.1

        options = []
        best = 999
        for cont in sorted_contours[:3]:
            if len(cont) < 5:
                continue 

            (x, y), (major_axis, minor_axis), angle = cv2.fitEllipse(cont)
            ellipse_area = np.pi * (major_axis / 2) * (minor_axis / 2)
            if 1.0 - TOLERANCE < ellipse_area / cv2.contourArea(cont) < 1.0 + TOLERANCE:
                if best > ellipse_area / cv2.contourArea(cont):
                    best = ellipse_area / cv2.contourArea(cont)
                    options = [x, y, 0]


        if len(options) == 0:
            return [999, 999, 999]

        return options

    def parseROI(self, roi, offset):
        roi = roi.copy()
        blurred_frame = cv2.GaussianBlur(roi, (5, 5), 0)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        all_contours = {}
        for color, c_range in COLOR_RANGES.items():
            if color == "orange":
                continue
            elif color == "red":
                red_mask_low = cv2.inRange(hsv_frame, c_range[0], c_range[1])
                red_mask_high = cv2.inRange(hsv_frame, c_range[2], c_range[3])
                mask = cv2.bitwise_or(red_mask_low, red_mask_high)
            else:
                mask = cv2.inRange(hsv_frame, c_range[0], c_range[1])


            kernel = np.ones((2, 2), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            cv2.imshow(f"mask {color}", mask)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            filtered_contours = [c for c in contours if cv2.contourArea(c) > (200 if USE_LOCAL else 40)]
            if len(filtered_contours) == 0:
                continue
        
            all_contours[color] = filtered_contours

        main_contours = [{"color": "yellow", "contour": c} for c in all_contours.get("yellow", [])] + [{"color": "blue", "contour": c} for c in all_contours.get("blue", [])]
        secondary_contours = []
        for color, contours in all_contours.items():
            if color not in ["yellow", "blue"]:
                for contour in contours:
                    secondary_contours.append({"color": color, "contour": contour})

        best = []
        for rect in main_contours:
            M_rect = cv2.moments(rect["contour"])
            center_rect = (int(M_rect["m10"] / M_rect["m00"]), int(M_rect["m01"] / M_rect["m00"]))
            neighbors = []
            for square in secondary_contours:
                M_sq = cv2.moments(square["contour"])
                center_sq = (int(M_sq["m10"] / M_sq["m00"]), int(M_sq["m01"] / M_sq["m00"]))
                neighbors.append((square, center_sq))

            if len(neighbors) < 2:
                continue
            
            min_dev = 999
            for sq_1, sq_2 in combinations(neighbors, 2):
                if sq_1[0]["color"] == sq_2[0]["color"] and not sq_1[0]["color"] in ("red", "purple"):
                    continue

                d1 = math.dist(center_rect, sq_1[1])
                d2 = math.dist(sq_1[1], sq_2[1])
                d3 = math.dist(sq_2[1], center_rect)
                distances = np.array([d1, d2, d3])
                avg_distance = np.mean(distances)
                relative_deviations = np.abs(distances - avg_distance) / avg_distance
                if np.all(relative_deviations <= PATTERN_TOLERANCE):
                    center = centroid(center_rect, sq_1[1], sq_2[1])
                    angle = bisectorAngle(center_rect, sq_1[1], sq_2[1])
                    if avg_distance < min_dev:
                        min_dev = avg_distance
                        best = [[center[0] + offset[0], center[1] + offset[1], angle], self.getID([sq_1[0]["color"], sq_2[0]["color"], rect["color"]]), avg_distance]

        if len(best) == 0:
            return [999, 999, 999], "", -1
        
        return best[0], best[1], best[2]

    def parseImage(self, frame, roi, offset):
        roi = roi.copy()
        frame = frame.copy()
        blurred_frame = cv2.GaussianBlur(roi, (5, 5), 0)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        all_contours = {}
        for color, c_range in COLOR_RANGES.items():
            
            if color == "red":
                red_mask_low = cv2.inRange(hsv_frame, (0, 100, 100), (10, 255, 255))
                red_mask_high = cv2.inRange(hsv_frame, (165, 100, 100), (180, 255, 255))
                mask = cv2.bitwise_or(red_mask_low, red_mask_high)
            else:
                mask = cv2.inRange(hsv_frame, c_range[0], c_range[1])

            kernel = np.ones((2, 2), np.uint8)  # you can change size
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
            #mask = cv2.inRange(hsv_frame, c_range[0], c_range[1])
            #cv2.imshow(f"mask {color}", mask)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if color == "orange":
                filtered_contours = [c for c in contours if cv2.contourArea(c) > 20]
                cv2.drawContours(frame, filtered_contours, -1, (255, 0, 255), 3)
                #cv2.imshow("orange mask", mask)
                #cv2.imshow("cont", frame)
            else:
                filtered_contours = [c for c in contours if cv2.contourArea(c) > 200]

            if len(filtered_contours) == 0:
                if color == "orange":
                    ball = [999, 999]
                continue

            #thing = roi.copy()
            #cv2.drawContours(thing, filtered_contours, -1, (255, 0, 255), -1)
            #cv2.imshow(f"contour {color}", thing)
        
            if color == "orange":
                sorted_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)
                M_rect = cv2.moments(sorted_contours[0])
                center_rect = (int(M_rect["m10"] / M_rect["m00"]) + offset[0], int(M_rect["m01"] / M_rect["m00"]) + offset[1])
                x, y = center_rect
                ball = [x, y]
                w = h = 40
                top_left = (x - w // 2, y - h // 2)
                bottom_right = (x + w // 2, y + h // 2)
                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
                cv2.putText(frame, "Ball", (x-15, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            else:
                all_contours[color] = filtered_contours

        main_contours = [{"color": "yellow", "contour": c} for c in all_contours.get("yellow", [])] + [{"color": "blue", "contour": c} for c in all_contours.get("blue", [])]
        secondary_contours = []
        for color, contours in all_contours.items():
            if color not in ["yellow", "blue"]:
                for contour in contours:
                    secondary_contours.append({"color": color, "contour": contour})

        #patterns = []
        seen = []
        for rect in main_contours:
            M_rect = cv2.moments(rect["contour"])
            center_rect = (int(M_rect["m10"] / M_rect["m00"]) + offset[0], int(M_rect["m01"] / M_rect["m00"]) + offset[1])
            neighbors = []
            for square in secondary_contours:
                M_sq = cv2.moments(square["contour"])
                center_sq = (int(M_sq["m10"] / M_sq["m00"]) + offset[0], int(M_sq["m01"] / M_sq["m00"]) + offset[1])
                #print(f"distance between {rect['color']} at {center_rect}, and {square['color']} at {center_sq}: {math.dist(center_rect, center_sq)}")
                if math.dist(center_rect, center_sq) < SEARCH_RADIUS:
                    neighbors.append((square, center_sq))

            if len(neighbors) < 2:
                #print(f"Not enough neighbors: {len(neighbors)}")
                continue
            #else:
            #    print(f"good pattern, neighbors: {len(neighbors)}")

            #cv2.circle(frame, center_rect, radius=3, color=(255, 0, 255), thickness=-1)
            for sq_1, sq_2 in combinations(neighbors, 2):
                if sq_1[0]["color"] == sq_2[0]["color"]:
                    continue

                #print("checking ", sq_1[0]["color"], sq_2[0]["color"])

                """
                distance_1 = math.dist(center_rect, sq_1[1])
                distance_2 = math.dist(center_rect, sq_2[1])
                if distance_1 == 0 or distance_2 == 0:
                    continue

                if 1-PATTERN_TOLERANCE < distance_1/distance_2 < 1+PATTERN_TOLERANCE:
                """
        
                d1 = math.dist(center_rect, sq_1[1])
                d2 = math.dist(sq_1[1], sq_2[1])
                d3 = math.dist(sq_2[1], center_rect)
                distances = np.array([d1, d2, d3])
                avg_distance = np.mean(distances)
                relative_deviations = np.abs(distances - avg_distance) / avg_distance
                if np.all(relative_deviations <= PATTERN_TOLERANCE):
                    center = centroid(center_rect, sq_1[1], sq_2[1])
                    angle = bisectorAngle(center_rect, sq_1[1], sq_2[1])
                    seen.append([[sq_1[0]["color"], sq_2[0]["color"], rect["color"]], distances, (center, angle, self.getID([sq_1[0]["color"], sq_2[0]["color"], rect["color"]]))])
                    """
                    #print(f"tolerance: {relative_deviations}")
 
                    print(f"{sq_1[1]} {sq_2[1]} {center_rect} angle: {angle}")
                    cv2.circle(frame, sq_1[1], radius=3, color=(255, 0, 0), thickness=-1)
                    cv2.circle(frame, sq_2[1], radius=3, color=(255, 0, 0), thickness=-1)
                    cv2.line(frame, sq_1[1], center_rect, color=(0, 0, 255), thickness=2)
                    cv2.line(frame, sq_2[1], center_rect, color=(0, 0, 255), thickness=2)
                    """

        #print("=== SEEN === ", seen)
        patterns = sorted(self.validate(seen), key=lambda x: x[2][2])
        #print("=== VALIDATED === ", patterns)
        res = [ball + [0]]
        items = {item[2][2]: item for item in patterns}
        #print("=== ITEMS === ", items)

        for i in range(1, 7):
            if i in items:
                p = items[i][2]
                angle_rad = math.radians(p[1])
                end_x = int(p[0][0] + 30 * math.cos(angle_rad))
                end_y = int(p[0][1] + 30 * math.sin(angle_rad))
                #cv2.line(frame, p[0], (end_x, end_y), color=(0, 0, 255), thickness=2)
                cv2.arrowedLine(frame, p[0], (end_x, end_y), (0, 0, 255), 2, tipLength=0.3)
                cv2.putText(frame, f"Robot {p[2]-1}", (p[0][0]-30, p[0][1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                res.append([p[0][0], p[0][1], p[1]])
            else:
                res.append([999, 999, 999])

        #print(f"Found {len(patterns)} patterns")
        """
        for p in patterns:res
            p = p[2]
            res.append([p[0][0], p[0][1], p[1]])
            #cv2.circle(frame, p[0], radius=5, color=(255, 255, 255), thickness=-1)
            angle_rad = math.radians(p[1])
            end_x = int(p[0][0] + 30 * math.cos(angle_rad))
            end_y = int(p[0][1] + 30 * math.sin(angle_rad))
            cv2.line(frame, p[0], (end_x, end_y), color=(0, 0, 255), thickness=2)
            cv2.putText(frame, f"Robot {p[2]}", (p[0][0]-30, p[0][1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        """

        return frame, res

    def validate(self, seen):
        from collections import defaultdict
        color_groups = defaultdict(list)
        for pattern in seen:
            colors, distances, data = pattern
            key = tuple(sorted(colors))
            color_groups[key].append((colors, distances, data))

        patterns = []
        for group in color_groups.values():
            if len(group) == 1:
                patterns.append(group[0])
            else:
                best = min(group, key=lambda x: np.average(x[1]))
                patterns.append(best)
        
        return patterns

    def getID(self, colors):
        if "yellow" in colors and "blue" in colors:
            return -1
        
        key = frozenset(colors)
        if key not in self.patterns:
            if "yellow" in colors:
                if self.next_yellow > 2:
                    return -1
                self.patterns[key] = self.next_yellow
                self.next_yellow += 1
            elif "blue" in colors:
                if self.next_blue > 2:
                    return -1
                self.patterns[key] = self.next_blue
                self.next_blue += 1
            else:
                return -1
        

        return f'{"yellow" if "yellow" in colors else "blue"}{self.patterns[key]}'

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
        print("init")
        self.publisher = self.create_publisher(FieldData, 'field_data', 10)
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model = YOLO(os.path.join(get_package_share_directory('sim'), 'models', 'yolo.pt'))
        self.model.to(device)
        self.registry = PatternRegistry()
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
            self.cam = cv2.VideoCapture(2)
            if not self.cam.isOpened():
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
            self.cam = cv2.VideoCapture(2)
            if not self.cam.isOpened():
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

            self.registry.reset()
    
    def camSetup(self):
        global CAM_EXPOSURE
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
        self.cam.set(cv2.CAP_PROP_EXPOSURE, CAM_EXPOSURE)

    def reset(self, msg, response):
        self.registry.reset()
        self.kalman.reset()
        self.prev = time.time()

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
        cv2.imshow("norm", norm)
        norm_copy = norm.copy()
        ball = self.registry.detectBall(norm)
        results = self.model(norm, verbose=False)
        accumulated = {label: [999, 999, 999, 999] for label in OBJ_LABELS}
        accumulated["Ball"] = ball
        for i, box in enumerate(results[0].boxes):
            coords_tensor = box.xyxy[0]
            coords = [int(val) for val in coords_tensor.tolist()]
            x1, y1, x2, y2 = coords
            confidence = box.conf.item()
            if confidence < 0.5:
                continue

            roi = norm[y1:y2, x1:x2]
            obs, label, avg_distance = self.registry.parseROI(roi, [x1, y1])
            if label in accumulated and accumulated[label][3] > avg_distance:
                accumulated[label] = obs + [avg_distance]

        observation = [accumulated[label][:3] for label in OBJ_LABELS]
        states = []
        curr = time.time()
        dt = curr - self.prev
        for i, obs in enumerate(observation):
            self.kalman[i].predict(dt)
            if obs[0] != 999:
                self.kalman[i].update(obs, [norm.shape[1], norm.shape[0]])
                self.seen[i] = time.time()
            
            if time.time() - self.seen[i] < DETECTION_TIMEOUT:
                state = self.kalman[i].getState()
                norm_copy = self.draw(norm_copy, state, OBJ_LABELS[i], 1 if TEAM_COLOR in OBJ_LABELS[i] else (0 if "Ball" in OBJ_LABELS[i] else -1))
                states.append(state)
                """
                if (1 <= i <= 3 and self.active[i-1]) or i == 0 or i > 3: 
                    state = self.kalman[i].getState()
                    norm_copy = self.draw(norm_copy, state, OBJ_LABELS[i], 1 if TEAM_COLOR in OBJ_LABELS[i] else (0 if "Ball" in OBJ_LABELS[i] else -1))
                    states.append(state)
                else:
                    states.append({
                        "x": 999.,
                        "y": 999.,
                        "theta": 999.,
                        "vx": 999.,
                        "vy": 999.,
                        "w": 999.,
                    })     
                """          
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
            obj_id = 0,
            current = True,
            x = data[0]["x"],
            y = data[0]["y"],
            theta = (math.degrees(data[0]["theta"])+90) % 360,
            vx = data[0]["vx"],
            vy = data[0]["vy"],
            w = data[0]["w"]
        )

        global TEAM_COLOR
        if TEAM_COLOR == "blue":
            order = [0, 4, 5, 6, 1, 2, 3]
        else:
            order = list(range(len(OBJ_LABELS)))

        for msg_index, i in enumerate(order[1:], start=1):
            robot = ObjData(
                obj_id = i,
                current = True,
                x = data[i]["x"],
                y = data[i]["y"],
                theta = (math.degrees(data[i]["theta"]) + 90) % 360,
                vx = data[i]["vx"],
                vy = data[i]["vy"],
                w = data[i]["w"]
            )
            setattr(msg, f'{"team" if msg_index < 4 else "op"}{(msg_index-1) % 3}', robot)

        return msg

    def srcCB(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.src_x, self.src_y = x, y
            cv2.circle(self.src, (x ,y), 5, (0, 0, 255), -1)

    def dstCB(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.dst_x, self.dst_y = x, y
            cv2.circle(self.dst, (x ,y), 5, (0, 0, 255), -1)

    def calibrate(self, src, bypass = False):
        if bypass:
            if USE_LOCAL:
                """
                self.H = np.array([
                    [1.37815360e+00, 5.54951443e-03, -1.20929691e+02],
                    [-2.28416795e-02, 9.55954974e-01, 5.12234601e+01],
                    [-1.97069052e-05, -2.71718704e-05, 1.00000000e+00]
                ])
                """
                """
                self.H = np.array([[     1.5022 ,  -0.036159   ,  -365.46],
                    [   0.011599     ,  1.025    ,   21.39],
                    [ 7.7535e-06 ,-4.0441e-05   ,        1]])
                """
                self.H = np.array([[     1.3794 ,   0.013779,     -297.26],
                    [  -0.028178  ,   0.95883     , 51.835],
                    [-3.2125e-05, -3.5546e-05  ,         1]])

            else:
                self.H = np.array([
                    [1.02222994e+00, -6.07657129e-03, -2.02668347e+00],
                    [-3.42416353e-03, 9.30203586e-01, 1.68165116e+01],
                    [1.11241564e-05, -3.17810579e-05, 1.00000000e+00]
                ])

                """
                H: [[      1.404    0.068012     -135.11]
 [  -0.019966      1.0104      41.707]
 [-2.6735e-05  5.2833e-05           1]]
 H: [[      1.396   -0.019535     -113.31]
 [  -0.021856     0.95574      48.693]
 [-2.6409e-07 -4.2463e-05           1]]

                """
            
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
                cv2.circle(self.src,(self.src_x, self.src_y), 5, (0, 255, 0), -1)
                cv2.circle(self.dst,(self.dst_x, self.dst_y), 5, (0, 255, 0), -1)
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
    
    def draw(self, frame, state, label, mod):
        h_px, w_px = frame.shape[0], frame.shape[1]

        scale_x = w_px / 17.0
        scale_y = h_px / 13.0

        x_px = int(state["x"] * scale_x + w_px / 2.0)
        y_px = int(h_px / 2.0 - state["y"] * scale_y)

        cv2.circle(frame, (x_px, y_px), 5, (0, 255, 0) if mod == 1 else ((255, 0, 255) if mod == 0 else (0, 0, 255)), -1)

        angle_rad = state["theta"]
        end_x = int(x_px + 20 * math.cos(angle_rad))
        end_y = int(y_px + 20 * math.sin(angle_rad))
        if mod != 0:
            cv2.arrowedLine(frame, (x_px, y_px), (end_x, end_y), (0, 255, 0) if mod == 1 else (0, 0, 255), 2, tipLength=0.3)
        else:
            cv2.rectangle(frame, (x_px-20, y_px-20), (x_px+20, y_px+20), (0, 255, 0), 3)

        cv2.putText(frame, label, (x_px-30, y_px-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        return frame
    
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