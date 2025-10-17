import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from sim_msgs.msg import LowCmd
import socket
import threading
import struct
import time

HEARTBEAT_TIMEOUT_S = 2.0 
LAPTOP_IP = "0.0.0.0"
HEARTBEAT_BASE_PORT = 9000
ANGLE_DAMP_FACTOR = 3
ROBOT_CONFIG = [
    {"ip": "192.168.0.123", "port": 8000, "max_speed": 5},
    {"ip": "192.168.0.216", "port": 8001, "max_speed": 3},
]
NUM_ROBOTS = len(ROBOT_CONFIG)

class Comms(Node):
    def __init__(self):
        super().__init__('comms')
        self.robot_status = [{'active': False, 'last_heartbeat': 0.0} for _ in range(NUM_ROBOTS)]
        self.active_mutex = threading.Lock()
        self.is_running = threading.Event()
        self.send_sockets = []
        self.recv_sockets = []
        for i in range(NUM_ROBOTS):
            try:
                recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                recv_socket.bind((LAPTOP_IP, HEARTBEAT_BASE_PORT + i))
                send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.recv_sockets.append(recv_socket)
                self.send_sockets.append(send_socket)
            except OSError as e:
                print(f"error: {e}")
                rclpy.shutdown()
                return

        self.active_publisher = self.create_publisher(Int32MultiArray, 'active', 10)
        self.cmd_subscribers = []
        for i in range(NUM_ROBOTS):
            sub = self.create_subscription(LowCmd, f'low{i}', lambda msg, i=i: self.lowCB(msg, i), 10)
            self.cmd_subscribers.append(sub)

        self.listener_threads = []
        for i in range(NUM_ROBOTS):
            thread = threading.Thread(target=lambda i=i: self.hbCB(i))
            thread.daemon = True
            self.listener_threads.append(thread)
            thread.start()

        self.active_thread = threading.Thread(target=self.activeCB)
        self.active_thread.daemon = True
        self.active_thread.start()
        #self.status_timer = self.create_timer(0.1, self.activeCB)
        self.get_logger().info("Setup done")
        self.flag = True
        self.prev_dtheta = 0
        self.kp = 0.2
        self.kd = 0.5

    def lowCB(self, msg: LowCmd, id: int):
        clamped_vx = int(msg.vx / ROBOT_CONFIG[id]["max_speed"] * 255)
        clamped_vy = int(msg.vy / ROBOT_CONFIG[id]["max_speed"] * 255)
        clamped_dtheta = int(msg.dtheta / ANGLE_DAMP_FACTOR)

        payload = struct.pack('iii', clamped_vx, clamped_vy, clamped_dtheta)
        self.send_sockets[id].sendto(payload, (ROBOT_CONFIG[id]["ip"], ROBOT_CONFIG[id]["port"]))

    def hbCB(self, id: int):
        while rclpy.ok() and not self.is_running.is_set():
            try:
                self.recv_sockets[id]
                with self.active_mutex:
                    self.robot_status[id]['active'] = True
                    self.robot_status[id]['last_heartbeat'] = time.time()
            except socket.error:
                break

    def activeCB(self):
        while rclpy.ok() and not self.is_running.is_set():
            active = []
            with self.active_mutex:
                for i in range(NUM_ROBOTS):
                    if time.time() - self.robot_status[i]['last_heartbeat'] > HEARTBEAT_TIMEOUT_S:
                        self.robot_status[i]['active'] = False
                    
                    active.append(1 if self.robot_status[i]['active'] else 0)

            msg = Int32MultiArray()
            msg.data = active
            self.active_publisher.publish(msg)
            time.sleep(0.1)

    def destroy_node(self):
        self.get_logger().info("Shutting down...")
        self.is_running.set()
        for i in range(NUM_ROBOTS):
            self.recv_sockets[i].close()
            self.send_sockets[i].close()
            pass

        self.active_thread.join()
        for thread in self.listener_threads:
            thread.join()

        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = Comms()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()