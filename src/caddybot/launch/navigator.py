from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    return LaunchDescription([
        LifecycleNode( package='caddybot_navigator',
                       namespace='caddybot',
                       executable='navigator',
                       name='navigator',
        ),
    ])
