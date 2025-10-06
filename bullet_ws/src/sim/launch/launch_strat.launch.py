from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessStart
from launch_ros.actions import Node

def generate_launch_description():
    service_call_cmd = [
        'ros2', 'service', 'call', '/sim/controller', 'sim_msgs/srv/Controller',
        '"{settings: {ball: {x: 999.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'robot0: {x: 0.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'robot1: {x: 0.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'robot2: {x: 0.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'robot3: {x: 0.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'robot4: {x: 0.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'robot5: {x: 0.0, y: 0.0, theta: 0.0, vx: 0.0, vy: 0.0, w: 0.0}, '
        'score1: 0, score2: 0}}"'
    ]

    return LaunchDescription([
        Node(
            package='sim',
            executable='strat',
            name='strat',
            output='screen'
        ),
        
        TimerAction(
            period=0.0,
            actions=[
                ExecuteProcess(
                    cmd=service_call_cmd,
                    shell=True,
                    output='screen'
                )
            ]
        )
    ])