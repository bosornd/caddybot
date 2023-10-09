from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    return LaunchDescription([
        LifecycleNode(
            package='caddybot_sound',
            namespace='caddybot',
            executable='sound_manager',
            name='sound_manager',
        ),
    ])