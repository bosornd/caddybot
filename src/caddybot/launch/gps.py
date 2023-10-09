from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='caddybot_gps',
            namespace='caddybot',
            executable='gps',       # 'fake_gps'
            name='gps',
            parameters=[
                {'gps': '/dev/pts/0'},
            ]
        ),
        Node(
            package='caddybot_gps',
            namespace='caddybot',
            executable='utm',
            name='utm',
        ),
    ])