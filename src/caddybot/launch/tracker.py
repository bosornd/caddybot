from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    params = os.path.join(get_package_share_directory('caddybot'), 'config', 'tracker.yaml')

    return LaunchDescription([
        LifecycleNode( package='caddybot_tracker',
                       executable='pov',
                       name='pov',
                       namespace='caddybot',
                       parameters=[params],
                       remappings=[
                            ('/scan/input', '/scan'),
                            ('/scan/output', '/scan/pov')
                       ],
        ),
        LifecycleNode( package='caddybot_tracker',
                       executable='avg',
                       name='avg',
                       namespace='caddybot',
                       parameters=[params],
                       remappings=[
                            ('/scan/input', '/scan/pov'),
                            ('/scan/output', '/scan/avg')
                       ],
        ),
        LifecycleNode( package='caddybot_tracker',
                       executable='tracker',
                       name='tracker',
                       namespace='caddybot',
                       parameters=[params],
                       remappings=[
                            ('/scan', '/scan/avg'),
                            ('/velocity', '/velocity/tracker')
                       ],
        ),
    ])

