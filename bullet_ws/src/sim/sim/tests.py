import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from ament_index_python.packages import get_package_share_directory
import os

COLOR_RANGES = {
    "red": [(0, 100, 100), (15, 255, 255), (165, 100, 100), (180, 255, 255)],
    "orange": [(5, 100, 100), (20, 255, 255)],
    "yellow": [(20, 25, 25), (38, 255, 255)],
    "green": [(38, 50, 50), (90, 255, 255)],
    "light_blue": [(90, 100, 100), (105, 255, 255)],
    "blue": [(105, 50, 50), (130, 255, 255)], 
    "purple": [(130, 50, 50), (165, 255, 255)]
}

class HSVFilterNode(Node):
    def __init__(self):
        super().__init__('hsv_filter_node')
        while True:
            frame = cv2.imread(os.path.join(get_package_share_directory('sim'), 'imgs', 'captura_10.png'))
            if frame is None:
                print("fail")
                return
            coords = self.detectBall(frame)
            if coords[0] != 999:
                print(coords)
                cv2.rectangle(frame, (int(coords[0]-10), int(coords[1]-10)), (int(coords[0]+10), int(coords[1]+10)), (255, 0, 255), 2)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)

    def detectBall(self, img):
        frame = img.copy()
        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, COLOR_RANGES["orange"][0], COLOR_RANGES["orange"][1])
        kernel = np.ones((2, 2), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("ball", mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        filtered_contours = [cont for cont in contours if cv2.contourArea(cont) > 40]
        if len(filtered_contours) == 0:
            return None
        
        sorted_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)

        TOLERANCE = 0.2
        options = []
        for cont in sorted_contours[:3]:
            if len(cont) < 5:
                continue 

            (x, y), (major_axis, minor_axis), angle = cv2.fitEllipse(cont)
            ellipse_area = np.pi * (major_axis / 2) * (minor_axis / 2)
            if 1.0 - TOLERANCE < ellipse_area / cv2.contourArea(cont) < 1.0 + TOLERANCE:
                options.append([x, y, ellipse_area / cv2.contourArea(cont)])

        if len(options) == 0:
            return None
        
        return options[0]
        


def main(args=None):
    rclpy.init(args=args)
    hsv_filter_node = HSVFilterNode()
    try:
        rclpy.spin(hsv_filter_node)
    except KeyboardInterrupt:
        pass
    finally:
        hsv_filter_node.destroy_node()
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
