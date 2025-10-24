import rclpy
from rclpy.node import Node
import tkinter as tk
from tkinter import ttk
from sensor_msgs.msg import Image
from sim_msgs.msg import Settings, HighCmd, FieldData, LowCmd, ObjData
from sim_msgs.srv import Controller, Reset
from cv_bridge import CvBridge
import cv2
from PIL import Image as PILImage, ImageTk
from enum import IntEnum
import math
import numpy as np
import threading
import time
import queue # <--- 1. IMPORT QUEUE

class State(IntEnum):
    HALT = -1
    PAUSE = 0
    PLAY = 1
    MIDFIELD = 2
    PENALTY = 3

# --- Default Settings ---
TEAM_COLOR = "yellow"
TEAM_SIDE = "right"
USE_LOCAL = True
CAM_EXPOSURE = 400
VIDEO_WIDTH = 2048
VIDEO_HEIGHT = 1080

FIELD_W = 17
FIELD_H = 13

class GUI(Node):
    def __init__(self):
        super().__init__('gui')
        self.root = tk.Tk()
        self.root.title("VSSS GUI")
        self.root.geometry("2800x1800")
        self.bridge = CvBridge()
        
        self.gui_queue = queue.Queue()
        self.color_var = tk.IntVar(value=1 if TEAM_COLOR == "yellow" else 0)
        self.side_var = tk.IntVar(value=1 if TEAM_SIDE == "right" else 0)
        self.local_var = tk.IntVar(value=1 if USE_LOCAL else 0)
        self.exposure_var = tk.IntVar(value=CAM_EXPOSURE)
        self.reset_var = False
        self.attractive_gain_var = tk.DoubleVar(value=0.5)
        self.repulsive_gain_var = tk.DoubleVar(value=3.)
        self.repulsion_radius_var = tk.DoubleVar(value=1.)
        self.tangential_gain_var = tk.DoubleVar(value=3.)
        self.goal_tolerance_var = tk.DoubleVar(value=0.0)
        self.target_offset_var = tk.DoubleVar(value=0.5)
        self.colinearity_var = tk.DoubleVar(value=0.97)

        self.video_subscriber1 = self.create_subscription(Image, 'local_cam/image_raw', self.image_callback, 10)
        self.video_subscriber2 = self.create_subscription(Image, 'sim_cam/image_raw', self.image_callback, 10)
        self.video_subscriber1 = self.create_subscription(FieldData, 'field_data', self.fieldCB, 10)
        self.cmd_subscribers = []
        for i in range(3):
            sub = self.create_subscription(LowCmd, f'low{i}', lambda msg, i=i: self.lowCB(msg, i), 10)
            self.cmd_subscribers.append(sub)
        self.settings_publisher = self.create_publisher(Settings, 'settings', 10)
        self.cmd_publishers = {
            0: self.create_publisher(LowCmd, '/low0', 10),
            1: self.create_publisher(LowCmd, '/low1', 10),
            2: self.create_publisher(LowCmd, '/low2', 10)
        }

        self.ros_clients = {
            'controller': self.create_client(Controller, 'strat/controller'),
        }
        self.client_ready = {name: False for name in self.ros_clients}
        for name, client in self.ros_clients.items():
            threading.Thread(
                target=self._wait_for_service,
                args=(name, client),
                daemon=True
            ).start()
        
        self.setup_gui()
        self.create_timer(0.05, self.update_gui) # 20 Hz
        self.create_timer(0.2, self.publish_settings)
        self.field_data = FieldData
        self.cmds = [None, None, None]

    def _wait_for_service(self, name, client):
        while not client.wait_for_service(timeout_sec=1.0):
            pass
        self.get_logger().info(f'{name} service is now available!')
        self.client_ready[name] = True

    def lowCB(self, msg, id):
        self.cmds[id] = msg

    def fieldCB(self, msg):
        self.field_data = msg

    def image_callback(self, msg):
        name = "huh"
        try:
            if not self.video_label.winfo_exists():
                return
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            resized_image = cv2.resize(cv_image, (VIDEO_WIDTH, VIDEO_HEIGHT), interpolation=cv2.INTER_AREA)
            rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

            coords = np.array(self.cvCoords((self.field_data.ball.x, self.field_data.ball.y)))
            if self.is_paused:
                cv2.rectangle(rgb_image, coords - 30, coords + 30, (0, 0, 255), 5)
            else:
                cv2.circle(rgb_image, coords, 8, (0, 0, 255), -1)
                vx_px = self.field_data.ball.vx * VIDEO_WIDTH / FIELD_W
                vy_px = -self.field_data.ball.vy * VIDEO_HEIGHT / FIELD_H
                if abs(vx_px) > 1 and abs(vy_px) > 1:
                    mag = math.sqrt(vx_px**2 + vy_px**2)
                    min_len = 50
                    max_len = 1000
                    if mag > 1e-6:
                        scale = max(min_len, min(max_len, mag)) / mag
                        vx_px *= scale
                        vy_px *= scale

                    end_x = int(coords[0] + vx_px)
                    end_y = int(coords[1] + vy_px)
                    cv2.arrowedLine(rgb_image, coords, (end_x, end_y), (255, 255, 0), 5, tipLength=0.2)

            for i in range(6):
                name = f'{"team" if i < 3 else "op"}{i%3}'
                robot = getattr(self.field_data, f'{"team" if i < 3 else "op"}{i%3}')
                coords = np.array(self.cvCoords((robot.x, robot.y)))
                cv2.putText(rgb_image, name, coords-60, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
                angle_rad = math.radians(robot.theta - 90)
                end_x = int(coords[0] + 50 * math.cos(angle_rad))
                end_y = int(coords[1] + 50 * math.sin(angle_rad))
                cv2.arrowedLine(rgb_image, coords, (end_x, end_y), (0, 255, 0) if i < 3 else (255, 0, 0), 5, tipLength=0.3)
                if self.is_paused:
                    cv2.rectangle(rgb_image, coords - 50, coords + 50, (0, 255, 0) if i < 3 else (255, 0, 0), 5)
                else:
                    cv2.circle(rgb_image, coords, 8, (0, 255, 0) if i < 3 else (255, 0, 0), -1)
                
                relevant = -1
                for j, el in enumerate(self.team_vals):
                    if el == i:
                        relevant = j

                if not self.is_paused and i < 3 and relevant != -1 and not self.cmds[relevant] is None:
                    vx_px = self.cmds[relevant].vx * VIDEO_WIDTH / FIELD_W
                    vy_px = -self.cmds[relevant].vy * VIDEO_HEIGHT / FIELD_H
                    if abs(vx_px) > 3 and abs(vy_px) > 3:
                        mag = math.sqrt(vx_px**2 + vy_px**2)
                        min_len = 50
                        max_len = 1000
                        if mag > 1e-6:
                            scale = max(min_len, min(max_len, mag)) / mag
                            vx_px *= scale
                            vy_px *= scale

                        end_x = int(coords[0] + vx_px)
                        end_y = int(coords[1] + vy_px)
                        cv2.arrowedLine(rgb_image, coords, (end_x, end_y), (255, 255, 0), 5, tipLength=0.2)

            pil_image = PILImage.fromarray(rgb_image)
            photo_image = ImageTk.PhotoImage(image=pil_image)
            self.video_label.config(image=photo_image, text="")
            self.video_label.image = photo_image
        except Exception as e:
            self.get_logger().error(f'Failed to process image: {e}, {name}')

    def setup_gui(self):
        # ... (Your GUI setup code is unchanged) ...
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = ttk.Frame(main_frame, padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        color_frame = ttk.LabelFrame(left_frame, text="Team Color", padding="10")
        color_frame.pack(fill=tk.X, pady=5)
        ttk.Radiobutton(color_frame, text="Yellow", variable=self.color_var, value=1).pack(anchor=tk.W)
        ttk.Radiobutton(color_frame, text="Blue", variable=self.color_var, value=0).pack(anchor=tk.W)

        side_frame = ttk.LabelFrame(left_frame, text="Field Side", padding="10")
        side_frame.pack(fill=tk.X, pady=5)
        ttk.Radiobutton(side_frame, text="Left", variable=self.side_var, value=0).pack(anchor=tk.W)
        ttk.Radiobutton(side_frame, text="Right", variable=self.side_var, value=1).pack(anchor=tk.W)

        local_frame = ttk.LabelFrame(left_frame, text="Source", padding="10")
        local_frame.pack(fill=tk.X, pady=5)
        ttk.Radiobutton(local_frame, text="USB", variable=self.local_var, value=1).pack(anchor=tk.W)
        ttk.Radiobutton(local_frame, text="Sim", variable=self.local_var, value=0).pack(anchor=tk.W)
        
        exposure_frame = ttk.LabelFrame(left_frame, text="Camera Exposure", padding="10")
        exposure_frame.pack(fill=tk.X, pady=5)
        exposure_slider = ttk.Scale(
            exposure_frame, from_=200, to=1000, orient=tk.HORIZONTAL,
            variable=self.exposure_var, length=200, command=self._on_exposure_change
        )
        exposure_slider.pack(anchor=tk.W, fill=tk.X, expand=True, pady=5)
        exposure_label = ttk.Label(exposure_frame, textvariable=self.exposure_var)
        exposure_label.pack(anchor=tk.CENTER)



        vector_frame = ttk.LabelFrame(left_frame, text="Potential Vector Field", padding="10")
        vector_frame.pack(fill=tk.X, pady=5)

        # Attractive Gain
        ttk.Label(vector_frame, text="Attractive Gain").pack(anchor=tk.W)
        attractive_gain_slider = ttk.Scale(
            vector_frame, from_=0, to=5, orient=tk.HORIZONTAL,
            variable=self.attractive_gain_var, length=200,
            command=lambda x: self.onVarChange(self.attractive_gain_var, x)
        )
        attractive_gain_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.attractive_gain_var).pack(anchor=tk.CENTER, pady=(0, 5))

        # Repulsive Gain
        ttk.Label(vector_frame, text="Repulsive Gain").pack(anchor=tk.W)
        repulsive_gain_slider = ttk.Scale(
            vector_frame, from_=0, to=5, orient=tk.HORIZONTAL,
            variable=self.repulsive_gain_var, length=200,
            command=lambda x: self.onVarChange(self.repulsive_gain_var, x)
        )
        repulsive_gain_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.repulsive_gain_var).pack(anchor=tk.CENTER, pady=(0, 5))

        # Repulsion Radius
        ttk.Label(vector_frame, text="Repulsion Radius").pack(anchor=tk.W)
        repulsion_radius_slider = ttk.Scale(
            vector_frame, from_=0, to=5, orient=tk.HORIZONTAL,
            variable=self.repulsion_radius_var, length=200,
            command=lambda x: self.onVarChange(self.repulsion_radius_var, x)
        )
        repulsion_radius_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.repulsion_radius_var).pack(anchor=tk.CENTER, pady=(0, 5))

        # Tangential Gain
        ttk.Label(vector_frame, text="Tangential Gain").pack(anchor=tk.W)
        tangential_gain_slider = ttk.Scale(
            vector_frame, from_=0, to=5, orient=tk.HORIZONTAL,
            variable=self.tangential_gain_var, length=200,
            command=lambda x: self.onVarChange(self.tangential_gain_var, x)
        )
        tangential_gain_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.tangential_gain_var).pack(anchor=tk.CENTER, pady=(0, 5))

        # Goal Tolerance
        ttk.Label(vector_frame, text="Goal Tolerance").pack(anchor=tk.W)
        goal_tolerance_slider = ttk.Scale(
            vector_frame, from_=0, to=5, orient=tk.HORIZONTAL,
            variable=self.goal_tolerance_var, length=200,
            command=lambda x: self.onVarChange(self.goal_tolerance_var, x)
        )
        goal_tolerance_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.goal_tolerance_var).pack(anchor=tk.CENTER, pady=(0, 5))

        ttk.Label(vector_frame, text="Target offset").pack(anchor=tk.W)
        target_offset_slider = ttk.Scale(
            vector_frame, from_=0, to=2, orient=tk.HORIZONTAL,
            variable=self.target_offset_var, length=200,
            command=lambda x: self.onVarChange(self.target_offset_var, x)
        )
        target_offset_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.target_offset_var).pack(anchor=tk.CENTER, pady=(0, 5))

        ttk.Label(vector_frame, text="Colinearity").pack(anchor=tk.W)
        colinearity_slider = ttk.Scale(
            vector_frame, from_=0.8, to=1, orient=tk.HORIZONTAL,
            variable=self.colinearity_var, length=200,
            command=lambda x: self.colinearity_var.set(x)
        )
        colinearity_slider.pack(anchor=tk.W, fill=tk.X, expand=True)
        ttk.Label(vector_frame, textvariable=self.colinearity_var).pack(anchor=tk.CENTER, pady=(0, 5))

        

        reset_button = ttk.Button(left_frame, text="Reset registry", command=self.buttonCB)
        reset_button.pack(pady=20)

        self.right_frame = ttk.LabelFrame(main_frame, text="Live feed", padding="10")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.video_label = ttk.Label(self.right_frame, anchor="center")
        self.video_label.pack(fill=tk.BOTH, expand=True)
        self.video_label.config(text="Waiting for video feed...")


        robot_frame = ttk.LabelFrame(left_frame, text="Robot Teams", padding="10")
        robot_frame.pack(fill=tk.X, pady=5)

        self.robot_team_vars = []
        self.robot_dropdowns = []
        self.team_vals = [-1, -1, -1]

        team_options = {"None": -1, "team0": 0, "team1": 1, "team2": 2}

        for i in range(3):
            ttk.Label(robot_frame, text=f"Robot {i}").pack(anchor=tk.W)

            var = tk.StringVar(value="None")
            dropdown = ttk.Combobox(
                robot_frame,
                textvariable=var,
                values=list(team_options.keys()),
                state="readonly"
            )
            dropdown.pack(fill=tk.X, pady=2)
            self.robot_team_vars.append((var, team_options))
            self.robot_dropdowns.append(dropdown)

        auto_button = ttk.Button(left_frame, text="Auto detect", command=self.autoCB)
        auto_button.pack(pady=20)


        # --- Control Buttons Underneath Video ---
        button_frame = ttk.Frame(self.right_frame)
        button_frame.pack(fill=tk.X, pady=10)

        # Toggleable Pause/Resume button
        self.is_paused = True
        self.pause_button = ttk.Button(button_frame, text="Resume", command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        # MIDFIELD button
        self.midfield_button = ttk.Button(button_frame, text="Midfield", command=lambda: self.call_controller(State.MIDFIELD))
        self.midfield_button.pack(side=tk.LEFT, padx=10)

        # PENALTY button
        self.penalty_button = ttk.Button(button_frame, text="Penalty", command=lambda: self.call_controller(State.PENALTY))
        self.penalty_button.pack(side=tk.LEFT, padx=10)

    def autoCB(self):
        if not self.call_controller(State.HALT):
            return

        self.current = 0
        self.auto_thread = threading.Thread(target=lambda: self.autoCheck(self.field_data), daemon=True)
        self.auto_thread.start()
        self.pause_button.config(text="Resume")
        self.is_paused = True

    def autoCheck(self, original):
        for i in range(3):
            self.gui_queue.put((i, "None"))

        for i in range(3):
            self.get_logger().info(f"Auto-detect: Testing physical robot {i}")
            cmd_0 = LowCmd(robot_id=0, vx=0., vy=0., dtheta=0.)
            cmd_1 = LowCmd(robot_id=0, vx=0., vy=0., dtheta=180.)
            original = self.field_data
            for j in range(3):
                if j == i:
                    self.cmd_publishers[j].publish(cmd_1)
                else:
                    self.cmd_publishers[j].publish(cmd_0)

            timeout = time.time()

            while time.time() - timeout < 2:
                if abs(original.team0.theta - self.field_data.team0.theta) > 90:
                    self.get_logger().info(f"robot{i} is team0. DIFF {original.team0.theta}, {self.field_data.team0.theta}")
                    self.gui_queue.put((i, "team0"))
                    break
                elif abs(original.team1.theta - self.field_data.team1.theta) > 90:
                    self.get_logger().info(f"robot{i} is team1, DIFF {original.team1.theta}, {self.field_data.team1.theta}")
                    self.gui_queue.put((i, "team1"))
                    break
                elif abs(original.team2.theta - self.field_data.team2.theta) > 90:
                    self.get_logger().info(f"obot{i} is team2 DIFF {original.team2.theta}, {self.field_data.team2.theta}")
                    self.gui_queue.put((i, "team2"))
                    break
                else:
                    time.sleep(0.1)

            self.cmd_publishers[i].publish(cmd_0)
            time.sleep(1)

        self.get_logger().info("Auto-detect complete.")
        self.call_controller(State.PAUSE)

    def toggle_pause(self):
        if self.is_paused:
            if not self.call_controller(State.PLAY):
                return
            self.pause_button.config(text="Pause")
        else:
            if not self.call_controller(State.PAUSE):
                return
            self.pause_button.config(text="Resume")
        self.is_paused = not self.is_paused

    def call_controller(self, state: State):
        if not self.client_ready["controller"] or not self.ros_clients["controller"].service_is_ready():
            self.get_logger().warn("Controller service not available.")
            return False

        req = Controller.Request()
        req.state = int(state)
        req.team0 = HighCmd(robot_id=0, skill=0, mod=0, tgt_x=0.0, tgt_y=0.0, tgt_theta=0.0)
        req.team1 = HighCmd(robot_id=1, skill=0, mod=0, tgt_x=0.0, tgt_y=0.0, tgt_theta=0.0)
        req.team2 = HighCmd(robot_id=2, skill=0, mod=0, tgt_x=0.0, tgt_y=0.0, tgt_theta=0.0)
        future = self.ros_clients["controller"].call_async(req)
        future.add_done_callback(self.controller_response)
        return True

    def controller_response(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info("Controller command executed successfully.")
                return
            else:
                self.get_logger().warn("Controller command failed.")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

        self.is_paused = not self.is_paused
        self.pause_button.config(text="Pause" if self.is_paused else "Resume")

    def onVarChange(self, var, value_str):
        value = float(value_str)
        new_value = round(value / 0.1) * 0.1
        var.set(new_value)
        
    def update_gui(self):
        self.process_gui_queue()
        if self.root.winfo_exists():
            self.root.update()
        else:
            rclpy.shutdown()
            
    def process_gui_queue(self):
        try:
            while not self.gui_queue.empty():
                index, value = self.gui_queue.get_nowait()
                if index < len(self.robot_dropdowns):
                    print(f"setting {index} as {value}")
                    self.robot_dropdowns[index].set(value)
        except queue.Empty:
            pass

    def publish_settings(self):
        msg = Settings()
        msg.team_color = bool(self.color_var.get())
        msg.team_side = bool(self.side_var.get())
        msg.exposure = self.exposure_var.get()
        msg.local = bool(self.local_var.get())
        msg.reset = self.reset_var
        msg.repulsive_gain = self.repulsive_gain_var.get()
        msg.repulsion_radius = self.repulsion_radius_var.get()
        msg.tangential_gain = self.tangential_gain_var.get()
        msg.goal_tolerance = self.goal_tolerance_var.get()
        msg.attractive_gain = self.attractive_gain_var.get()
        msg.target_offset = self.target_offset_var.get()
        msg.colinearity = self.colinearity_var.get()

        for i, (var, team_options) in enumerate(self.robot_team_vars):
            setattr(msg, f"robot{i}", team_options[var.get()])
            self.team_vals[i] = team_options[var.get()]

        self.settings_publisher.publish(msg)

    def buttonCB(self):
        self.reset_var = not self.reset_var

    def _on_exposure_change(self, value_str):
        value = float(value_str)
        new_value = int(round(value / 20.0) * 20)
        self.exposure_var.set(new_value)

    def cvCoords(self, coords):
        scale_x = VIDEO_WIDTH / FIELD_W
        scale_y = VIDEO_HEIGHT / FIELD_H
        return [int((coords[0] + FIELD_W / 2) * scale_x), int((FIELD_H / 2 - coords[1]) * scale_y)]

def main(args=None):
    rclpy.init(args=args)
    node = GUI()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.root.winfo_exists():
            node.root.destroy()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()