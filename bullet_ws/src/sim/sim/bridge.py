import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from sim_msgs.msg import LowCmd
import threading
import struct
import time
import numpy as np
import serial
import serial.tools.list_ports

HEARTBEAT_TIMEOUT_S = 2.0 

SERIAL_CMD_HEADER = b'\xAA\xBB'
SERIAL_HB_HEADER_1 = 0xCC
SERIAL_HB_HEADER_2 = 0xDD
BAUD_RATE = 115200

ANGLE_DAMP_FACTOR = 3
OFFSET = [20, 20, 25]

class Comms(Node):
    def __init__(self):
        super().__init__('comms')

        self.robot_status = [{'active': False, 'last_heartbeat': 0.0} for _ in range(3)]
        self.latest_cmds = [LowCmd() for _ in range(3)] 
        self.active_mutex = threading.Lock()
        self.is_running = threading.Event()

        self.declare_parameter('serial_port', 'auto')
        port_setting = self.get_parameter('serial_port').get_parameter_value().string_value
        
        ports_to_try = []
        if port_setting == 'auto':
            ports_to_try = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyUSB2']
        else:
            ports_to_try = [port_setting]

        self.serial_port = None
        for port_name in ports_to_try:
            try:
                self.serial_port = serial.Serial(port_name, BAUD_RATE, timeout=0.1)
                self.get_logger().info(f"Successfully connected to serial port: {port_name}")
                break
            except serial.SerialException as e:
                self.get_logger().warn(f"Failed to open port {port_name}: {e}. Trying next...")

        if self.serial_port is None:
            self.get_logger().error(f"Could not connect to any of the attempted ports: {ports_to_try}")
            self.get_logger().warn("Available serial ports:")
            ports = serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                self.get_logger().warn(f"  {port}: {desc} [{hwid}]")
            rclpy.shutdown()
            return

        self.active_publisher = self.create_publisher(Int32MultiArray, 'active', 10)
        self.cmd_subscribers = []
        for i in range(3):
            sub = self.create_subscription(LowCmd, f'low{i}', lambda msg, i=i: self.lowCB(msg, i), 10)
            self.cmd_subscribers.append(sub)
        
        self.send_timer = self.create_timer(0.0333, self.send_serial_packet)
        self.read_thread = threading.Thread(target=self.serial_read_loop)
        self.read_thread.daemon = True

        self.active_thread = threading.Thread(target=self.activeCB)
        self.active_thread.daemon = True

        self.read_thread.start()
        self.active_thread.start()

    def lowCB(self, msg: LowCmd, robot_id: int):
        self.latest_cmds[robot_id] = msg

    def send_serial_packet(self):
        full_payload = bytearray()
        for i in range(3):
            cmd = self.latest_cmds[i]
            
            clamped_vx = int(cmd.vx * 255)
            clamped_vy = int(cmd.vy * 255)

            clamped_dtheta = int(cmd.dtheta / 4)

            payload_part = struct.pack('iii', clamped_vx, clamped_vy, clamped_dtheta)
            full_payload.extend(payload_part)
        
        payload_len = len(full_payload)
        packet_to_send = SERIAL_CMD_HEADER + struct.pack('B', payload_len) + full_payload

        try:
            self.serial_port.write(packet_to_send)
        except serial.SerialException as e:
            self.get_logger().error(f"Serial write error: {e}")
            self.is_running.set()
            rclpy.shutdown()

    def serial_read_loop(self):
        state = "WAIT_HEADER_1"
        payload_len = 0
        payload_buffer = bytearray()

        while rclpy.ok() and not self.is_running.is_set():
            try:
                byte_in = self.serial_port.read(1)
                if not byte_in:
                    continue

                byte_val = byte_in[0]

                if state == "WAIT_HEADER_1":
                    if byte_val == SERIAL_HB_HEADER_1:
                        state = "WAIT_HEADER_2"
                
                elif state == "WAIT_HEADER_2":
                    if byte_val == SERIAL_HB_HEADER_2:
                        state = "WAIT_LEN"
                    else:
                        state = "WAIT_HEADER_1"
                
                elif state == "WAIT_LEN":
                    payload_len = byte_val
                    payload_buffer.clear()
                    state = "WAIT_DATA"

                elif state == "WAIT_DATA":
                    payload_buffer.append(byte_val)
                    if len(payload_buffer) == payload_len:
                        self.process_heartbeat(payload_buffer)
                        state = "WAIT_HEADER_1"
            
            except serial.SerialException as e:
                self.get_logger().error(f"Serial read error: {e}. Shutting down.")
                self.is_running.set()
                rclpy.shutdown()
            except Exception as e:
                self.get_logger().error(f"Error in read loop: {e}")
                state = "WAIT_HEADER_1"

    def process_heartbeat(self, payload: bytearray):
        if len(payload) == 1:
            try:
                robot_id = struct.unpack('B', payload)[0]

                if 0 <= robot_id < len(self.robot_status):
                    with self.active_mutex:
                        self.robot_status[robot_id]['active'] = True
                        self.robot_status[robot_id]['last_heartbeat'] = time.time()
                else:
                    self.get_logger().warn(f"Received heartbeat from invalid robot_id: {robot_id}")
            except struct.error as e:
                self.get_logger().warn(f"Failed to unpack heartbeat: {e}")
        else:
             self.get_logger().warn(f"Received packet with unexpected length: {len(payload)}")


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
        self.get_logger().info("Shutting down comms node...")
        self.is_running.set()
        
        if self.read_thread.is_alive():
            self.read_thread.join(timeout=1.0)
        if self.active_thread.is_alive():
            self.active_thread.join(timeout=1.0)

        if hasattr(self, 'serial_port') and self.serial_port.is_open:
            self.serial_port.close()
            self.get_logger().info("Serial port closed.")

        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = Comms()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroyNode()
            rclpy.shutdown()

if __name__ == '__main__':
    main()