from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    params = os.path.join(get_package_share_directory('caddybot'), 'config', 'zone.yaml')

    return LaunchDescription([
        LifecycleNode( package='caddybot_zone',
                       executable='zone',
                       name='zone',
                       namespace='caddybot',
                       parameters=[params],
        ),
        LifecycleNode( package='caddybot_zone',
                       executable='zone_controller',
                       name='zone_controller',
                       namespace='caddybot',
                       parameters=[params],
                       remappings=[
                            ('/velocity/input', '/velocity/tracker'),
                            ('/velocity/output', '/velocity'),
                       ],
        ),
    ])

