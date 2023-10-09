from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    return LaunchDescription([
        LifecycleNode(
            package='caddybot_gps',
            namespace='caddybot',
            executable='fake_gps',
            name='gps',
        ),
        LifecycleNode(
            package='caddybot_gps',
            namespace='caddybot',
            executable='utm',
            name='utm',
        ),
    ])