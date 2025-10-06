import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from sim_msgs.msg import LowCmd

import socket
import threading
import struct
import time
import math

# --- Configuration ---
NUM_ROBOTS = 2
HEARTBEAT_TIMEOUT_S = 2.0 

LAPTOP_IP = "0.0.0.0"
HEARTBEAT_BASE_PORT = 9990

MAX_LINEAR_SPEED = 3

ROBOT_CONFIG = [
    {"ip": "192.168.100.163", "port": 8889},
    {"ip": "192.168.100.165", "port": 8890},
]

class UdpRelayNode(Node):
    def __init__(self):
        super().__init__('comms')
        self.get_logger().info("UDP Relay Node starting up...")

        # --- State Tracking ---
        self.robot_status = [
            {'active': False, 'last_heartbeat_time': 0.0} for _ in range(NUM_ROBOTS)
        ]
        self.status_lock = threading.Lock()

        # --- Network Setup ---
        # A single socket for sending commands to all robots
        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # A list of sockets, one for each robot's heartbeat
        self.recv_sockets = []
        for i in range(NUM_ROBOTS):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.bind((LAPTOP_IP, HEARTBEAT_BASE_PORT + i))
                self.recv_sockets.append(sock)
                self.get_logger().info(f"Bound to {LAPTOP_IP}:{HEARTBEAT_BASE_PORT + i} for Robot {i} heartbeats.")
            except OSError as e:
                self.get_logger().error(f"Failed to bind heartbeat socket for Robot {i}: {e}")
                rclpy.shutdown()
                return

        # --- ROS2 Publishers and Subscribers ---
        self.active_publisher = self.create_publisher(Int32MultiArray, 'active', 10)
        self.subs = []
        for i in range(NUM_ROBOTS):
            sub = self.create_subscription(
                LowCmd,
                f'low{i}',
                lambda msg, robot_id=i: self.command_callback(msg, robot_id),
                10
            )
            self.subs.append(sub)

        # --- Threads ---
        self.running = True
        self.listener_threads = []
        for i in range(NUM_ROBOTS):
            thread = threading.Thread(target=self.heartbeat_listener, args=(i,))
            thread.daemon = True
            self.listener_threads.append(thread)
            thread.start()

        self.status_timer = self.create_timer(0.1, self.publish_status_callback)
        self.get_logger().info("Node setup complete. Listening for commands and heartbeats.")

    def command_callback(self, msg: LowCmd, robot_id: int):
        #speed = math.sqrt(msg.vx**2 + msg.vy**2)
        clamped_vx = int(msg.vx / 3 * 255)
        clamped_vy = int(msg.vy / 3 * 255)
        clamped_dtheta = int(msg.dtheta)
        payload = struct.pack('iii', clamped_vx, clamped_vy, clamped_dtheta)
        #payload = struct.pack('fff', msg.vx, msg.vy, msg.dtheta)
        
        target_ip = ROBOT_CONFIG[robot_id]["ip"]
        target_port = ROBOT_CONFIG[robot_id]["port"]
        
        self.send_socket.sendto(payload, (target_ip, target_port))

    def heartbeat_listener(self, robot_id: int):
        """Dedicated thread to listen for a specific robot's heartbeat."""
        sock = self.recv_sockets[robot_id]
        self.get_logger().info(f"Heartbeat listener for Robot {robot_id} started.")
        while self.running:
            try:
                # We don't need the data, just the fact that we received something
                data, addr = sock.recvfrom(1024) 
                with self.status_lock:
                    self.robot_status[robot_id]['active'] = True
                    self.robot_status[robot_id]['last_heartbeat_time'] = time.time()
            except socket.error:
                # This can happen on shutdown
                break
        self.get_logger().info(f"Heartbeat listener for Robot {robot_id} stopping.")

    def publish_status_callback(self):
        """Periodically checks for timeouts and publishes the active status."""
        active_list = []
        current_time = time.time()
        
        with self.status_lock:
            for i in range(NUM_ROBOTS):
                # Check for timeout
                if current_time - self.robot_status[i]['last_heartbeat_time'] > HEARTBEAT_TIMEOUT_S:
                    self.robot_status[i]['active'] = False
                
                active_list.append(1 if self.robot_status[i]['active'] else 0)

        msg = Int32MultiArray()
        msg.data = active_list
        self.active_publisher.publish(msg)

    def destroy_node(self):
        self.get_logger().info("Shutting down...")
        self.running = False
        # Close all sockets to unblock the listener threads
        self.send_socket.close()
        for sock in self.recv_sockets:
            sock.close()
        # Wait for threads to finish
        for thread in self.listener_threads:
            thread.join()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = UdpRelayNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()