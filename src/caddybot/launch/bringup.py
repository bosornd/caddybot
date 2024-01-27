import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
   dir = os.path.join(get_package_share_directory('caddybot'), 'launch')

   return LaunchDescription([
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/fake_gps.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/map.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/positioner.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/fake_lidar.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/tracker.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/navigator.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/sound.py'])
      ),
      IncludeLaunchDescription(
         PythonLaunchDescriptionSource([dir, '/mcu.py'])
      ),
   ])
