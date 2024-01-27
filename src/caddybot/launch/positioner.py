from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    return LaunchDescription([
        LifecycleNode( package='caddybot_positioner',
                       namespace='caddybot',
                       executable='positioner',
                       name='positioner',
        ),
    ])
