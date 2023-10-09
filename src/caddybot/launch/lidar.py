from launch import LaunchDescription
from launch_ros.actions import LifecycleNode

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    params = os.path.join(get_package_share_directory('lslidar_driver'), 'params', 'lsx10.yaml')

    return LaunchDescription([
        LifecycleNode( package='lslidar_driver',
                       executable='lslidar_driver_node',
                       name='lidar',
                       namespace='caddybot',
                       parameters=[params],
        ),
    ])

