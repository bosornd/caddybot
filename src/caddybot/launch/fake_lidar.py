from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    return LaunchDescription([
        LifecycleNode(
            package='caddybot_lidar',
            namespace='caddybot',
            executable='lidar',
            name='lidar',
        ),
    ])