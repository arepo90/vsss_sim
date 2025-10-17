import rclpy
from rclpy.node import Node
import tkinter as tk
from tkinter import ttk
from sensor_msgs.msg import Image
from sim_msgs.msg import Settings
from cv_bridge import CvBridge
import cv2
from PIL import Image as PILImage, ImageTk

# --- Default Settings ---
TEAM_COLOR = "yellow"
TEAM_SIDE = "right"
USE_LOCAL = True
CAM_EXPOSURE = 400
VIDEO_WIDTH = 2048
VIDEO_HEIGHT = 1080

class GUI(Node):
    def __init__(self):
        super().__init__('gui')
        self.root = tk.Tk()
        self.root.title("VSSS GUI")
        self.root.geometry("2800x1600")
        self.bridge = CvBridge()

        # --- Tkinter Control Variables ---
        self.color_var = tk.IntVar(value=1 if TEAM_COLOR == "yellow" else 0)
        self.side_var = tk.IntVar(value=1 if TEAM_SIDE == "right" else 0)
        self.local_var = tk.IntVar(value=1 if USE_LOCAL else 0)
        self.exposure_var = tk.IntVar(value=CAM_EXPOSURE)
        self.reset_var = False
        self.attractive_gain_var = tk.DoubleVar(value=0.5)
        self.repulsive_gain_var = tk.DoubleVar(value=3.)
        self.repulsion_radius_var = tk.DoubleVar(value=1.)
        self.tangential_gain_var = tk.DoubleVar(value=3.)
        self.goal_tolerance_var = tk.DoubleVar(value=1.)

        # --- ROS2 Publishers & Subscribers ---
        self.video_subscriber1 = self.create_subscription(Image, 'local_cam/image_raw', self.image_callback, 10)
        self.video_subscriber2 = self.create_subscription(Image, 'sim_cam/image_raw', self.image_callback, 10)
        self.settings_publisher = self.create_publisher(Settings, 'settings', 10)
        
        # --- Build the GUI ---
        self.setup_gui()
        
        # --- ROS Timers for All Loops ---
        self.create_timer(0.05, self.update_gui) # 20 Hz
        self.create_timer(0.2, self.publish_settings)

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
            exposure_frame, from_=200, to=600, orient=tk.HORIZONTAL,
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

        

        reset_button = ttk.Button(left_frame, text="Reset registry", command=self.buttonCB)
        reset_button.pack(pady=20)

        self.right_frame = ttk.LabelFrame(main_frame, text="Live feed", padding="10")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.video_label = ttk.Label(self.right_frame, anchor="center")
        self.video_label.pack(fill=tk.BOTH, expand=True)
        self.video_label.config(text="Waiting for video feed...")

    def onVarChange(self, var, value_str):
        value = float(value_str)
        new_value = round(value / 0.5) * 0.5
        var.set(new_value)
        
    def update_gui(self):
        if self.root.winfo_exists():
            self.root.update()
        else:
            self.get_logger().info("GUI window closed by user.")
            rclpy.shutdown()

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
        self.settings_publisher.publish(msg)

    def image_callback(self, msg):
        try:
            if not self.video_label.winfo_exists():
                return
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            resized_image = cv2.resize(cv_image, (VIDEO_WIDTH, VIDEO_HEIGHT), interpolation=cv2.INTER_AREA)
            rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
            pil_image = PILImage.fromarray(rgb_image)
            photo_image = ImageTk.PhotoImage(image=pil_image)
            self.video_label.config(image=photo_image, text="")
            self.video_label.image = photo_image
        except Exception as e:
            self.get_logger().error(f'Failed to process image: {e}')

    def buttonCB(self):
        self.reset_var = not self.reset_var

    def _on_exposure_change(self, value_str):
        value = float(value_str)
        new_value = int(round(value / 20.0) * 20)
        self.exposure_var.set(new_value)

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