import rclpy
from rclpy.node import Node
import tkinter as tk
from tkinter import ttk
import threading
from sensor_msgs.msg import Image
from sim_msgs.msg import Settings
from cv_bridge import CvBridge
import cv2
from PIL import Image as PILImage, ImageTk
import time

# --- Default Settings ---
FRIENDLY_COLOR = "yellow"  # "yellow" or "blue"
FRIENDLY_SIDE = "right"    # "right" or "left"
USE_LOCAL = True
CAM_EXPOSURE = 400
VIDEO_WIDTH = 960
VIDEO_HEIGHT = 540

class GUI(Node):
    def __init__(self):
        super().__init__('gui')
        self.root = tk.Tk()
        self.root.title("VSSS GUI")
        self.root.geometry("1280x720")
        self.bridge = CvBridge()

        # --- Tkinter Control Variables ---
        self.color_var = tk.IntVar(value=0 if FRIENDLY_COLOR == "yellow" else 1)
        self.side_var = tk.IntVar(value=1 if FRIENDLY_SIDE == "right" else 0)
        self.local_var = tk.IntVar(value=1 if USE_LOCAL else 0)
        self.exposure_var = tk.IntVar(value=CAM_EXPOSURE)
        self.check_vars = []

        # --- ROS2 Publishers & Subscribers ---
        self.video_subscriber = self.create_subscription(Image, 'camera/image_raw', self.image_callback, 10)
        self.settings_publisher = self.create_publisher(Settings, 'settings', 10)
        
        # --- Threading ---
        self.is_running = threading.Event()
        self.settings_thread = threading.Thread(target=self.publish_settings_loop)
        self.settings_thread.start()
        
        self.setup()

    def setup(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = ttk.Frame(main_frame, padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # --- Color Selection ---
        color_frame = ttk.LabelFrame(left_frame, text="Team Color", padding="10")
        color_frame.pack(fill=tk.X, pady=5)
        ttk.Radiobutton(color_frame, text="Yellow", variable=self.color_var, value=1).pack(anchor=tk.W)
        ttk.Radiobutton(color_frame, text="Blue", variable=self.color_var, value=0).pack(anchor=tk.W)

        # --- Side Selection ---
        side_frame = ttk.LabelFrame(left_frame, text="Field Side", padding="10")
        side_frame.pack(fill=tk.X, pady=5)
        ttk.Radiobutton(side_frame, text="Left", variable=self.side_var, value=0).pack(anchor=tk.W)
        ttk.Radiobutton(side_frame, text="Right", variable=self.side_var, value=1).pack(anchor=tk.W)

        local_frame = ttk.LabelFrame(left_frame, text="Field Side", padding="10")
        local_frame.pack(fill=tk.X, pady=5)
        ttk.Radiobutton(local_frame, text="USB", variable=self.local_var, value=1).pack(anchor=tk.W)
        ttk.Radiobutton(local_frame, text="Sim", variable=self.local_var, value=0).pack(anchor=tk.W)
        
        # --- Camera Exposure Slider ---
        exposure_frame = ttk.LabelFrame(left_frame, text="Camera Exposure", padding="10")
        exposure_frame.pack(fill=tk.X, pady=5)
        exposure_slider = ttk.Scale(
            exposure_frame,
            from_=200,  
            to=600,
            orient=tk.HORIZONTAL,
            variable=self.exposure_var,
            length=200,
            command=self._on_exposure_change
        )
        exposure_slider.pack(anchor=tk.W, fill=tk.X, expand=True, pady=5)
        exposure_label = ttk.Label(exposure_frame, textvariable=self.exposure_var)
        exposure_label.pack(anchor=tk.CENTER)

        # --- Video Feed Frame ---
        self.right_frame = ttk.LabelFrame(main_frame, text="Live feed", padding="10")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.video_label = ttk.Label(self.right_frame, anchor="center")
        self.video_label.pack(fill=tk.BOTH, expand=True)
        self.video_label.config(text="Waiting for video feed...")

    def _on_exposure_change(self, value_str):
        value = float(value_str)
        new_value = int(round(value / 20.0) * 20)
        self.exposure_var.set(new_value)

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            resized_image = cv2.resize(cv_image, (VIDEO_WIDTH, VIDEO_HEIGHT), interpolation=cv2.INTER_AREA)
            rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
            pil_image = PILImage.fromarray(rgb_image)
            photo_image = ImageTk.PhotoImage(image=pil_image)
            self.video_label.config(image=photo_image, text="")
            self.video_label.image = photo_image
        except Exception as e:
            self.get_logger().error(f'Failed to process image: {e}')

    def publish_settings_loop(self):
        while rclpy.ok() and not self.is_running.is_set():
            # 1. Instantiate the message with ()
            msg = Settings() 
            
            # 2. Populate the fields, converting int to bool
            msg.friendly_color = bool(self.color_var.get())   # e.g., bool(0) is False, bool(1) is True
            msg.friendly_side = bool(self.side_var.get())
            msg.exposure = self.exposure_var.get()
            msg.local = bool(self.local_var.get())
            
            self.settings_publisher.publish(msg)
            time.sleep(0.2)

    def run(self):
        self.root.mainloop()

    def destroyNode(self):
        self.get_logger().info('Shutting down GUI and ROS node.')
        self.is_running.set()
        self.settings_thread.join()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = GUI()
    spin_thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    spin_thread.start()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroyNode()
        rclpy.shutdown()

if __name__ == '__main__':
    main()