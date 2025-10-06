import cv2
import numpy as np
import math
from itertools import combinations
import os
import time
import socket
import pickle
import threading # Make sure threading is imported

MIN_AREA = 40
SEARCH_RADIUS = 40
PATTERN_TOLERANCE = 0.25
COLOR_RANGES = {
    "red": [(0, 100, 100), (10, 255, 255)], "orange": [(10, 100, 100), (20, 255, 255)],
    "yellow": [(20, 25, 25), (38, 255, 255)], "green": [(38, 50, 50), (85, 255, 255)],
    "light_blue": [(85, 100, 100), (105, 255, 255)], "blue": [(105, 50, 50), (130, 255, 255)],
    "purple": [(130, 50, 50), (165, 255, 255)]
}

# ==============================================================================
# 1. COMMUNICATIONS LIBRARY (Unchanged)
# ==============================================================================
# This port map must be IDENTICAL to the one in the other scripts.
TOPIC_PORTS = {
    'camera/image_raw': 10001, '/low0': 10002, '/low1': 10003, '/low2': 10004,
    'score1': 10005, 'score2': 10006, 'sim/controller': 10007, 'field_data': 10008,
}

class UDPCommunicator:
    # ... (This class remains exactly the same as before) ...
    """A simple UDP-based communicator to replace ROS2 pub/sub and services."""
    def __init__(self):
        self.subscribers = {}
        self.threads = []
        self.running = True
    def publish(self, topic, data):
        if topic not in TOPIC_PORTS: return
        port = TOPIC_PORTS[topic]
        payload = pickle.dumps(data)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(payload, ('<broadcast>', port))
    def subscribe(self, topic, callback):
        if topic not in TOPIC_PORTS: return
        port = TOPIC_PORTS[topic]
        self.subscribers[port] = callback
        thread = threading.Thread(target=self._listen_topic, args=(port,), daemon=True)
        self.threads.append(thread)
        thread.start()
    def _listen_topic(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', port))
            while self.running:
                try:
                    payload, _ = s.recvfrom(65536)
                    data = pickle.loads(payload)
                    if isinstance(data, tuple) and data[0] == 'image':
                        img = cv2.imdecode(data[1], cv2.IMREAD_COLOR)
                        self.subscribers[port](img)
                    else:
                        self.subscribers[port](data)
                except Exception as e:
                    print(f"Error while listening on port {port}: {e}")
    def shutdown(self):
        self.running = False


# ==============================================================================
# 2. MESSAGE DEFINITIONS (Unchanged)
# ==============================================================================
class ObjData:
    """Replicates sim_msgs/msg/ObjData"""
    def __init__(self, obj_id=0, current=False, x=0.0, y=0.0, theta=0.0, vx=0.0, vy=0.0, w=0.0):
        self.obj_id, self.current = obj_id, current; self.x, self.y, self.theta = x, y, theta; self.vx, self.vy, self.w = vx, vy, w
class FieldData:
    """Replicates sim_msgs/msg/FieldData"""
    def __init__(self):
        self.ball = ObjData(); self.robot0=ObjData(); self.robot1=ObjData(); self.robot2=ObjData()
        self.robot3=ObjData(); self.robot4=ObjData(); self.robot5=ObjData(); self.score1=0; self.score2=0


# ==============================================================================
# 3. VISION CORE LOGIC (Mostly Unchanged)
# ==============================================================================
# --- (All helper functions and the PatternRegistry and Kalman classes are unchanged) ---
def get_img_path(filename):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, '..', 'imgs', filename)

def bisectorAngle(P, A, B):
    P, u, v = np.array(P, dtype=float), np.array(A, dtype=float) - P, np.array(B, dtype=float) - P
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    if nu == 0 or nv == 0: raise ValueError("Vertex equals one of the other points")
    u, v = u / nu, v / nv
    w = u + v
    if np.linalg.norm(w) == 0: w = np.array([-u[1], u[0]])
    return (math.degrees(math.atan2(w[1], w[0])) + 360) % 360

def centroid(A, B, C):
    return ((A[0] + B[0] + C[0]) // 3, (A[1] + B[1] + C[1]) // 3)

class PatternRegistry:
    def __init__(self): self.patterns, self.next_id = {}, 1
    def reset(self): self.patterns, self.next_id = {}, 1
    def parseImage(self, frame):
        frame_copy = frame.copy(); hsv_frame = cv2.cvtColor(cv2.GaussianBlur(frame, (5, 5), 0), cv2.COLOR_BGR2HSV)
        all_contours, ball = {}, [999, 999]
        for color, c_range in COLOR_RANGES.items():
            if color == "red": mask = cv2.bitwise_or(cv2.inRange(hsv_frame, (0, 100, 100), (10, 255, 255)), cv2.inRange(hsv_frame, (165, 100, 100), (180, 255, 255)))
            else: mask = cv2.inRange(hsv_frame, c_range[0], c_range[1])
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE); area = 40 if color == "orange" else MIN_AREA
            filtered_contours = [c for c in contours if cv2.contourArea(c) > area]
            if not filtered_contours: continue
            if color == "orange":
                M = cv2.moments(sorted(filtered_contours, key=cv2.contourArea, reverse=True)[0]); center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                ball = list(center); cv2.rectangle(frame_copy, (center[0]-20, center[1]-20), (center[0]+20, center[1]+20), (0, 255, 0), 2)
                cv2.putText(frame_copy, "Ball", (center[0]-15, center[1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            else: all_contours[color] = filtered_contours
        main_contours = [{"color": c, "contour": cont} for c in ["yellow", "blue"] for cont in all_contours.get(c, [])]
        secondary_contours = [{"color": c, "contour": cont} for c, conts in all_contours.items() if c not in ["yellow", "blue"] for cont in conts]
        seen = []
        for rect in main_contours:
            M_rect = cv2.moments(rect["contour"]); center_rect = (int(M_rect["m10"] / M_rect["m00"]), int(M_rect["m01"] / M_rect["m00"]))
            neighbors = []
            for square in secondary_contours:
                M_sq = cv2.moments(square["contour"]); center_sq = (int(M_sq["m10"] / M_sq["m00"]), int(M_sq["m01"] / M_sq["m00"]))
                if math.dist(center_rect, center_sq) < SEARCH_RADIUS: neighbors.append((square, center_sq))
            if len(neighbors) < 2: continue
            for sq_1, sq_2 in combinations(neighbors, 2):
                if sq_1[0]["color"] == sq_2[0]["color"]: continue
                distances = np.array([math.dist(center_rect, sq_1[1]), math.dist(sq_1[1], sq_2[1]), math.dist(sq_2[1], center_rect)])
                if np.all(np.abs(distances - np.mean(distances)) / np.mean(distances) <= PATTERN_TOLERANCE):
                    center = centroid(center_rect, sq_1[1], sq_2[1]); angle = bisectorAngle(center_rect, sq_1[1], sq_2[1])
                    colors = [sq_1[0]["color"], sq_2[0]["color"], rect["color"]]; seen.append([colors, distances, (center, angle, self.getID(colors))])
        patterns = sorted(self.validate(seen), key=lambda x: x[2][2]); res = [ball + [0]]; items = {item[2][2]: item for item in patterns}
        for i in range(1, 7):
            if i in items:
                p = items[i][2]; angle_rad = math.radians(p[1]); end_pt = (int(p[0][0] + 30 * math.cos(angle_rad)), int(p[0][1] + 30 * math.sin(angle_rad)))
                cv2.arrowedLine(frame_copy, p[0], end_pt, (0, 0, 255), 2, tipLength=0.3)
                cv2.putText(frame_copy, f"Robot {p[2]-1}", (p[0][0]-30, p[0][1]-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                res.append([p[0][0], p[0][1], p[1]])
            else: res.append([999, 999, 999])
        return frame_copy, res
    def validate(self, seen):
        from collections import defaultdict
        color_groups = defaultdict(list)
        for pattern in seen: color_groups[tuple(sorted(pattern[0]))].append(pattern)
        return [min(group, key=lambda x: np.average(x[1])) if len(group)>1 else group[0] for group in color_groups.values()]
    def getID(self, colors):
        key = frozenset(colors)
        if key not in self.patterns:
            if self.next_id > 6: return -1
            self.patterns[key] = self.next_id; self.next_id += 1
        return self.patterns[key]
    
class Kalman:
    def __init__(self, id):
        self.id = id; self.x = np.zeros((6, 1)); self.P = np.eye(6) * 1.0; self.H = np.array([[1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,1,0,0,0]])
        self.Q = np.diag([3e-6, 3e-6, 1e-6, 0.002, 0.002, 0.005]); self.R = np.diag([4e-3, 4e-3, 1e-3]); self.I = np.eye(6)
        self.field_width_m, self.field_height_m = 17, 13
    def reset(self): self.x, self.P = np.zeros((6, 1)), np.eye(6) * 1.0
    def predict(self, dt): F = np.eye(6); F[0, 3], F[1, 4], F[2, 5] = dt, dt, dt; self.x = F @ self.x; self.P = F @ self.P @ F.T + self.Q; return self.x.flatten()
    def update(self, z_raw, px_dims):
        x_px, y_px, angle_deg = z_raw; scale_x, scale_y = self.field_width_m / px_dims[0], self.field_height_m / px_dims[1]
        x_m = (x_px - px_dims[0] / 2.0) * scale_x; y_m = (px_dims[1] / 2.0 - y_px) * scale_y
        angle_rad = np.arctan2(np.sin(math.radians(angle_deg)), np.cos(math.radians(angle_deg))); z = np.array([[x_m], [y_m], [angle_rad]])
        y = z - self.H @ self.x; y[2] = (y[2] + np.pi) % (2 * np.pi) - np.pi
        S = self.H @ self.P @ self.H.T + self.R; K = self.P @ self.H.T @ np.linalg.inv(S); self.x += K @ y; self.P = (self.I - K @ self.H) @ self.P
        return self.x.flatten()
    def getState(self): state = self.x.flatten(); return {"x": state[0], "y": state[1], "theta": state[2], "vx": state[3], "vy": state[4], "w": state[5]}


# --- Main Vision Class (Modified for threading) ---
class Vision:
    def __init__(self):
        self.comms = UDPCommunicator()
        self.registry = PatternRegistry()
        self.kalman = [Kalman(i) for i in range(7)]
        self.is_calibrated = False
        self.prev = time.time()
        self.score = [0, 0]

        # ---- CHANGED: Step 1 ----
        # Add a thread-safe buffer for the latest frame
        self.latest_frame_processed = None
        self.latest_frame_kalman = None
        self.frame_lock = threading.Lock()
        # -------------------------

        self.comms.subscribe('camera/image_raw', self.visionCB)
        self.comms.subscribe('score1', lambda score: self.scoreCB(0, score))
        self.comms.subscribe('score2', lambda score: self.scoreCB(1, score))
        print("Vision node running and subscribed to topics.")

    def scoreCB(self, id, score_value):
        self.score[id] = score_value

    def visionCB(self, img):
        # ---- CHANGED: Step 2 ----
        # This callback now ONLY processes data and stores the result.
        # It does NOT call cv2.imshow().
        if not self.is_calibrated:
            self.H = np.array([
                [1.02222994e+00, -6.07657129e-03, -2.02668347e+00],
                [-3.42416353e-03, 9.30203586e-01, 1.68165116e+01],
                [1.11241564e-05, -3.17810579e-05, 1.00000000e+00]])
            self.is_calibrated = True
            print("Homography matrix loaded.")
        
        norm = cv2.warpPerspective(img, self.H, (img.shape[1], img.shape[0]))
        norm_copy = norm.copy()
        frame, observation = self.registry.parseImage(norm)
        
        states = []
        dt = time.time() - self.prev
        for i, obs in enumerate(observation):
            self.kalman[i].predict(dt)
            if obs[0] != 999:
                self.kalman[i].update(obs, [frame.shape[1], frame.shape[0]])
            state = self.kalman[i].getState()
            if obs[0] != 999:
                norm_copy = self.draw(norm_copy, state)
            states.append(state)
        self.prev = time.time()
        
        field_data = self.getMsg(states)
        self.comms.publish('field_data', field_data)

        # Store the final images in the thread-safe buffer
        with self.frame_lock:
            self.latest_frame_processed = frame
            self.latest_frame_kalman = norm_copy
        # -------------------------

    # --- (getMsg and draw methods are unchanged) ---
    def getMsg(self, data):
        msg = FieldData(); msg.ball = ObjData(obj_id=0, current=True, x=data[0]["x"], y=data[0]["y"], theta=(math.degrees(data[0]["theta"])+90)%360, vx=data[0]["vx"], vy=data[0]["vy"], w=data[0]["w"])
        for i in range(1, 7):
            robot_data = data[i]; robot = ObjData(obj_id=i, current=True, x=robot_data["x"], y=robot_data["y"], theta=(math.degrees(robot_data["theta"])+90)%360, vx=robot_data["vx"], vy=robot_data["vy"], w=robot_data["w"])
            setattr(msg, f'robot{i-1}', robot)
        msg.score1, msg.score2 = self.score[0], self.score[1]; return msg
    def draw(self, frame, state):
        color = (0, 255, 0) if abs(state["vx"]) > 0.05 or abs(state["vy"]) > 0.05 else (0, 0, 255); h_px, w_px = frame.shape[:2]
        scale_x, scale_y = w_px / 17.0, h_px / 13.0; x_px = int(state["x"] * scale_x + w_px / 2.0); y_px = int(h_px / 2.0 - state["y"] * scale_y)
        cv2.circle(frame, (x_px, y_px), 5, color, -1); end_vel = (x_px + int(state["vx"] * scale_x * 4), y_px + int(-state["vy"] * scale_y * 4))
        cv2.arrowedLine(frame, (x_px, y_px), end_vel, color, 2, tipLength=0.3); end_theta = (int(x_px + 20 * math.cos(state["theta"])), int(y_px + 20 * math.sin(state["theta"])))
        cv2.arrowedLine(frame, (x_px, y_px), end_theta, (255, 0, 0), 2, tipLength=0.3); return frame

    def shutdown(self):
        self.comms.shutdown(); cv2.destroyAllWindows(); print("Vision node shut down.")

# ==============================================================================
# 4. MAIN EXECUTION BLOCK
# ==============================================================================
def main():
    node = Vision()
    print("Press 'q' in any OpenCV window to quit.")
    try:
        # ---- CHANGED: Step 3 ----
        # The main loop is now responsible for displaying the images
        while True:
            frame_to_show_processed = None
            frame_to_show_kalman = None

            with node.frame_lock:
                if node.latest_frame_processed is not None:
                    frame_to_show_processed = node.latest_frame_processed.copy()
                if node.latest_frame_kalman is not None:
                    frame_to_show_kalman = node.latest_frame_kalman.copy()

            if frame_to_show_processed is not None:
                cv2.imshow("Detected Patterns", frame_to_show_processed)
            if frame_to_show_kalman is not None:
                cv2.imshow("Kalman Filter Visualization", frame_to_show_kalman)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        # -------------------------
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt caught, shutting down.")
    finally:
        node.shutdown()

if __name__ == '__main__':
    main()