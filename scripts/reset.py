#!/usr/bin/env python3
import subprocess
import json

def call_controller_service():
    request_data = {
        'settings': {
            'ball': {'x': 999.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'robot0': {'x': 0.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'robot1': {'x': 0.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'robot2': {'x': 0.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'robot3': {'x': 0.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'robot4': {'x': 0.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'robot5': {'x': 0.0, 'y': 0.0, 'theta': 0.0, 'vx': 0.0, 'vy': 0.0, 'w': 0.0},
            'score1': 0,
            'score2': 0
        }
    }
    
    request_json = json.dumps(request_data)
    
    # Build the command
    cmd = [
        'ros2', 'service', 'call', '/sim/controller', 'sim_msgs/srv/Controller',
        request_json
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Service call successful!")
        print("Output:", result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Service call failed with error: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    except FileNotFoundError:
        print("Error: ros2 command not found. Make sure ROS2 is sourced.")

if __name__ == '__main__':
    call_controller_service()