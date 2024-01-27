from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

def generate_launch_description():

    return LaunchDescription([
        LifecycleNode( package='caddybot_tracker',
                       executable='segmenter',
                       name='segmenter',
                       namespace='caddybot',
        ),
        LifecycleNode( package='caddybot_tracker',
                       executable='tracker',
                       name='tracker',
                       namespace='caddybot',
        ),
    ])

