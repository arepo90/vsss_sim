import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from sim_msgs.msg import FieldData, ObjData
from std_msgs.msg import Int32
import cv2
import numpy as np
import math
from itertools import combinations
import os
import time

MIN_AREA = 40
SEARCH_RADIUS = 40
PATTERN_TOLERANCE = 0.25
COLOR_RANGES = {
    "red": [(0, 100, 100), (10, 255, 255)],
    "orange": [(10, 100, 100), (20, 255, 255)],
    "yellow": [(20, 25, 25), (38, 255, 255)],
    "green": [(38, 50, 50), (85, 255, 255)],
    "light_blue": [(85, 100, 100), (105, 255, 255)],
    "blue": [(105, 50, 50), (130, 255, 255)], 
    "purple": [(130, 50, 50), (165, 255, 255)]
}
"""
#original
COLOR_RANGES = {
    "orange": [(10, 100, 100), (20, 255, 255)],
    "yellow": [(20, 100, 100), (30, 255, 255)],
    "red": [(0, 100, 100), (10, 255, 255)],
    "blue": [(100, 150, 50), (130, 255, 255)], 
    "light_blue": [(85, 100, 100), (99, 255, 255)],
    "green": [(40, 50, 50), (80, 255, 255)],
    "purple": [(130, 50, 50), (160, 255, 255)]
}
"""

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

def centroid(A, B, C):
    x = (A[0] + B[0] + C[0]) // 3
    y = (A[1] + B[1] + C[1]) // 3
    return (x, y)

class PatternRegistry:
    def __init__(self):
        self.patterns = {}
        self.next_id = 1

    def reset(self):
        self.patterns = {}
        self.next_id = 1

    def parseImage(self, frame):
        frame = frame.copy()
        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        all_contours = {}
        for color, c_range in COLOR_RANGES.items():
            
            if color == "red":
                red_mask_low = cv2.inRange(hsv_frame, (0, 100, 100), (10, 255, 255))
                red_mask_high = cv2.inRange(hsv_frame, (165, 100, 100), (180, 255, 255))
                mask = cv2.bitwise_or(red_mask_low, red_mask_high)
            else:
                mask = cv2.inRange(hsv_frame, c_range[0], c_range[1])
        
            #mask = cv2.inRange(hsv_frame, c_range[0], c_range[1])
            #cv2.imshow(f"mask {color}", mask)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if color == "orange":
                filtered_contours = [c for c in contours if cv2.contourArea(c) > 40]
            else:
                filtered_contours = [c for c in contours if cv2.contourArea(c) > MIN_AREA]

            if len(filtered_contours) == 0:
                if color == "orange":
                    ball = [999, 999]
                continue

            #thing = frame.copy()
            #cv2.drawContours(thing, filtered_contours, -1, (255, 0, 255), -1)
            #cv2.imshow(f"contour {color}", thing)
        
            if color == "orange":
                sorted_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)
                M_rect = cv2.moments(sorted_contours[0])
                center_rect = (int(M_rect["m10"] / M_rect["m00"]), int(M_rect["m01"] / M_rect["m00"]))
                x, y = center_rect
                ball = [x, y]
                w = h = 40
                top_left = (x - w // 2, y - h // 2)
                bottom_right = (x + w // 2, y + h // 2)
                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
                cv2.putText(frame, "Ball", (center_rect[0]-15, center_rect[1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
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
            center_rect = (int(M_rect["m10"] / M_rect["m00"]), int(M_rect["m01"] / M_rect["m00"]))
            neighbors = []
            for square in secondary_contours:
                M_sq = cv2.moments(square["contour"])
                center_sq = (int(M_sq["m10"] / M_sq["m00"]), int(M_sq["m01"] / M_sq["m00"]))
                #print(f"distance between {rect['color']} at {center_rect}, and {square['color']} at {center_sq}: {math.dist(center_rect, center_sq)}")
                if math.dist(center_rect, center_sq) < SEARCH_RADIUS:
                    neighbors.append((square, center_sq))

            if len(neighbors) < 2:
                #print(f"Not enough neighbors: {len(neighbors)}")
                continue
            #else:
                #print(f"good pattern, neighbors: {len(neighbors)}")

            #cv2.circle(frame, center_rect, radius=3, color=(255, 0, 255), thickness=-1)
            for sq_1, sq_2 in combinations(neighbors, 2):
                if sq_1[0]["color"] == sq_2[0]["color"]:
                    continue

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
                TOLERANCE = 0.15
                if np.all(relative_deviations <= PATTERN_TOLERANCE):
                    center = centroid(center_rect, sq_1[1], sq_2[1])
                    angle = bisectorAngle(center_rect, sq_1[1], sq_2[1])
                    seen.append([[sq_1[0]["color"], sq_2[0]["color"], rect["color"]], distances, (center, angle, self.getID([sq_1[0]["color"], sq_2[0]["color"], rect["color"]]))])
                    """
                    #print(f"tolerance: {relative_deviations}")
 
                    #print(f"{sq_1[1]} {sq_2[1]} {center_rect} angle: {angle}")
                    #cv2.circle(frame, sq_1[1], radius=3, color=(255, 0, 0), thickness=-1)
                    #cv2.circle(frame, sq_2[1], radius=3, color=(255, 0, 0), thickness=-1)
                    cv2.line(frame, sq_1[1], center_rect, color=(0, 0, 255), thickness=2)
                    cv2.line(frame, sq_2[1], center_rect, color=(0, 0, 255), thickness=2)
                    pattern_ID = self.getID([sq_1[0]["color"], sq_2[0]["color"], rect["color"]])
                    if pattern_ID != -1:
                        patterns.append((center, angle, pattern_ID))
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
        key = frozenset(colors)
        if key not in self.patterns:
            if self.next_id > 6:
                return -1
            self.patterns[key] = self.next_id
            self.next_id += 1

        return self.patterns[key]
    
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
        
        #Q_diag = [1e-4, 1e-4, 1e-4, 1e-2, 1e-2, 1e-2]
        Q_diag = [3e-6, 3e-6, 1e-6, 0.002, 0.002, 0.005]
        #R_diag = [0.05, 0.05, 0.01]
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

        #angle_rad_raw = (90.0 - angle_deg) * np.pi / 180.0
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
        self.publisher = self.create_publisher(FieldData, 'field_data', 10)
        self.cv_bridge = CvBridge()
        self.registry = PatternRegistry()
        self.kalman = [Kalman(i) for i in range(7)]
        self.is_calibrated = False
        self.prev = time.time()
        self.src_list = []
        self.dst_list = []
        self.score = [0, 0]
        self.video_subscriber = self.create_subscription(Image, 'camera/image_raw', self.visionCB, 10)
        self.score1_subscriber = self.create_subscription(Int32, 'score1', lambda msg: self.scoreCB(0, msg), 10)
        self.score2_subscriber = self.create_subscription(Int32, 'score2', lambda msg: self.scoreCB(1, msg), 10)

    def reset(self, msg, response):
        self.registry.reset()
        self.kalman.reset()
        self.prev = time.time()
        self.score = [0, 0]

    def scoreCB(self, id, msg):
        self.score[id] = msg.data

    def visionCB(self, msg):
        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        if not self.is_calibrated:
            cv2.namedWindow('src')
            cv2.namedWindow('dst')
            cv2.setMouseCallback('src', self.srcCB)
            cv2.setMouseCallback('dst', self.dstCB)
            self.is_calibrated = self.calibrate(img.copy(), True) # mod
            cv2.destroyWindow('src')
            cv2.destroyWindow('dst')
        
        norm = cv2.warpPerspective(img, self.H, (img.shape[1], img.shape[0]))
        norm_copy = norm.copy()
        frame, observation = self.registry.parseImage(norm)
        #print("=== OBSERVATION === ", observation[1])
        states = []
        curr = time.time()
        dt = curr - self.prev
        for i, obs in enumerate(observation):
            self.kalman[i].predict(dt)
            if obs[0] != 999:
                self.kalman[i].update(obs, [frame.shape[1], frame.shape[0]])
            
            state = self.kalman[i].getState()
            if obs[0] != 999:
                norm_copy = self.draw(norm_copy, state)
            states.append(state)
        self.prev = curr
        #print("=== KALMAN === ", states[1])
        field_data = self.getMsg(states)
        self.publisher.publish(field_data)
        cv2.imshow("kalman", norm_copy)
        cv2.imshow("frame", frame)
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
        for i in range(1, 7):
            robot = ObjData(
                obj_id = i,
                current = True,
                x = data[i]["x"],
                y = data[i]["y"],
                theta = (math.degrees(data[i]["theta"])+90) % 360,
                vx = data[i]["vx"],
                vy = data[i]["vy"],
                w = data[i]["w"]
            )
            setattr(msg, f'robot{i-1}', robot)
        
        msg.score1 = self.score[0]
        msg.score2 = self.score[1]

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
            self.H = np.array([
                [1.02222994e+00, -6.07657129e-03, -2.02668347e+00],
                [-3.42416353e-03, 9.30203586e-01, 1.68165116e+01],
                [1.11241564e-05, -3.17810579e-05, 1.00000000e+00]
            ])
            return True
        self.src = src
        self.dst = cv2.imread(os.path.join(get_package_share_directory('sim'), 'imgs', 'dst.png'))
        self.dst = cv2.resize(self.dst, (self.src.shape[1], self.src.shape[0]))
        print('S - Save pair\nH - End')
        while True:
            cv2.imshow('src', self.src)
            cv2.imshow('dst', self.dst)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                print('Pair saved')
                cv2.circle(self.src,(self.src_x, self.src_y), 5, (0, 255, 0), -1)
                cv2.circle(self.dst,(self.dst_x, self.dst_y), 5, (0, 255, 0), -1)
                self.src_list.append([self.src_x, self.src_y])
                self.dst_list.append([self.dst_x, self.dst_y])
            elif k == ord('h'):
                src_pts = np.array(self.src_list).reshape(-1, 1, 2)
                dst_pts = np.array(self.dst_list).reshape(-1, 1, 2)
                H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5)
                self.H = H
                print("H: ", H)
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
    
    def draw(self, frame, state, color=(255, 255, 255)):
        if abs(state["vx"]) < 0.05 and abs(state["vy"]) < 0.05:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        h_px, w_px = frame.shape[0], frame.shape[1]

        scale_x = w_px / 17.0
        scale_y = h_px / 13.0

        x_px = int(state["x"] * scale_x + w_px / 2.0)
        y_px = int(h_px / 2.0 - state["y"] * scale_y)

        cv2.circle(frame, (x_px, y_px), 5, color, -1)

        vx_px = int(state["vx"] * scale_x)
        vy_px = int(-state["vy"] * scale_y)

        end_x = x_px + vx_px * 4
        end_y = y_px + vy_px * 4

        cv2.arrowedLine(frame, (x_px, y_px), (end_x, end_y), color, 2, tipLength=0.3)
    
        angle_rad = state["theta"]
        end_x = int(x_px + 20 * math.cos(angle_rad))
        end_y = int(y_px + 20 * math.sin(angle_rad))
        #cv2.line(frame, p[0], (end_x, end_y), color=(0, 0, 255), thickness=2)
        cv2.arrowedLine(frame, (x_px, y_px), (end_x, end_y), (0, 0, 255), 2, tipLength=0.3)

        return frame

def main(args=None):
    rclpy.init(args=args)
    node = Vision()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()