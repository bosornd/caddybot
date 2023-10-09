from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='caddybot_gps',
            namespace='caddybot',
            executable='fake_gps',
            name='gps'
        ),
    ])