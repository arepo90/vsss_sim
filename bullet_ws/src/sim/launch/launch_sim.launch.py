from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sim',
            executable='sim',
            name='sim',
            output='screen'
        ),
        Node(
            package='sim',
            executable='vision',
            name='vision',
            output='screen'
        ),
    ])
