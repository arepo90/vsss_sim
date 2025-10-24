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
ANGLE_DAMP_FACTOR = 5
BROADCAST_IP = "<broadcast>"
BROADCAST_PORT = 8888
ROBOT_CONFIG = [5, 3, 3]

class Comms(Node):
    def __init__(self):
        super().__init__('comms')
        self.robot_status = [{'active': False, 'last_heartbeat': 0.0} for _ in range(3)]
        self.latest_cmds = [LowCmd() for _ in range(3)] 
        self.active_mutex = threading.Lock()
        self.is_running = threading.Event()
        try:
            self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except OSError as e:
            self.get_logger().error(f"Failed to create broadcast socket: {e}")
            rclpy.shutdown()
            return

        self.recv_sockets = []
        for i in range(3):
            try:
                recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                recv_socket.bind((LAPTOP_IP, HEARTBEAT_BASE_PORT + i))
                self.recv_sockets.append(recv_socket)
            except OSError as e:
                self.get_logger().error(f"Failed to bind heartbeat socket for robot {i}: {e}")
                rclpy.shutdown()
                return

        self.active_publisher = self.create_publisher(Int32MultiArray, 'active', 10)
        self.cmd_subscribers = []
        for i in range(3):
            sub = self.create_subscription(LowCmd, f'low{i}', lambda msg, i=i: self.lowCB(msg, i), 10)
            self.cmd_subscribers.append(sub)
        
        self.send_timer = self.create_timer(0.01, self.send_broadcast_packet)
        self.listener_threads = []
        for i in range(3):
            thread = threading.Thread(target=lambda i=i: self.hbCB(i))
            self.listener_threads.append(thread)
            thread.start()

        self.active_thread = threading.Thread(target=self.activeCB)
        self.active_thread.daemon = True
        self.active_thread.start()

    def lowCB(self, msg: LowCmd, robot_id: int):
        self.latest_cmds[robot_id] = msg

    def send_broadcast_packet(self):
        full_payload = bytearray()
        for i in range(3):
            cmd = self.latest_cmds[i]
            clamped_vx = int(cmd.vx / ROBOT_CONFIG[i] * 255)
            clamped_vy = int(cmd.vy / ROBOT_CONFIG[i] * 255)
            clamped_dtheta = int(cmd.dtheta / ANGLE_DAMP_FACTOR)
            payload_part = struct.pack('iii', clamped_vx, clamped_vy, clamped_dtheta)
            full_payload.extend(payload_part)
        
        self.broadcast_socket.sendto(full_payload, (BROADCAST_IP, BROADCAST_PORT))

    def hbCB(self, robot_id: int):
        while rclpy.ok() and not self.is_running.is_set():
            try:
                self.recv_sockets[robot_id].recvfrom(1024) 
                with self.active_mutex:
                    self.robot_status[robot_id]['active'] = True
                    self.robot_status[robot_id]['last_heartbeat'] = time.time()
            except socket.error:
                break

    def activeCB(self):
        while rclpy.ok() and not self.is_running.is_set():
            active_list = []
            with self.active_mutex:
                for i in range(3):
                    if time.time() - self.robot_status[i]['last_heartbeat'] > HEARTBEAT_TIMEOUT_S:
                        self.robot_status[i]['active'] = False
                    
                    active_list.append(1 if self.robot_status[i]['active'] else 0)

            msg = Int32MultiArray()
            msg.data = active_list
            self.active_publisher.publish(msg)
            time.sleep(0.1)

    def destroyNode(self):
        self.is_running.set()
        self.broadcast_socket.close()
        for sock in self.recv_sockets:
            sock.close()

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
        node.destroyNode()
        rclpy.shutdown()

if __name__ == '__main__':
    main()