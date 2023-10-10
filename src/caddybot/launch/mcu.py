from launch import LaunchDescription
from launch_ros.actions import Node

import os

def generate_launch_description():
     return LaunchDescription([
          Node( package='micro_ros_agent',
                executable='micro_ros_agent',
                name='micro_ros_agent',
                namespace='caddybot',
                arguments=['udp4', '--port', '8888']
          )
     ])

