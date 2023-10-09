from launch import LaunchDescription
from launch_ros.actions import Node

import os

def generate_launch_description():
     agent = Node( package='micro_ros_agent',
                   executable='micro_ros_agent',
                   name='micro_ros_agent',
                   namespace='caddybot',
                   arguments=['udp4', '-p', '8888']
     )

     os.environ['RMW_IMPLEMENTATION'] = 'rmw_microxrcedds'
     mcu = Node( package='caddybot_mcu',
                 executable='mcu',
                 name='mcu',
                 namespace='caddybot_mcu',
     )

     return LaunchDescription([
               agent,
               mcu
     ])

