from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    return LaunchDescription([
        LifecycleNode(
            package='caddybot_gps',
            namespace='caddybot',
            executable='gps',
            name='gps',
            parameters=[
                {'gps': '/dev/pts/0'},  # gps device
            ]
        ),
        LifecycleNode(
            package='caddybot_gps',
            namespace='caddybot',
            executable='utm',
            name='utm',
        ),
    ])