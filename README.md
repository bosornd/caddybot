# caddybot
caddybot project for training

## ros2 vnc environment
```
C:\> docker run -p 8080:80 -it --name ros2 tiryoh/ros2-desktop-vnc:humble
```
connect to localhost:8008 in the browser (Edge is better)

## build
1. update packages
```
$ sudo apt update && sudo apt upgrade
```
2. git clone
```
$ git clone --recursive https://github.com/bosornd/caddybot.git
$ cd caddybot
```
3. install dependencies
```
$ rosdep install --from-paths src --ignore-src --rosdistro humble -y
```
```
$ pip install pygame
$ pip install pyserial sparkfun-ublox-gps utm
```
4. build
```
$ colcon build
$ source install/setup.bash
```
5. build micro_ros_agent for MCU
```
$ ros2 run micro_ros_setup create_agent_ws.sh
$ ros2 run micro_ros_setup build_agent.sh
```

## launch
using terminal1(ROS2),
```
$ source install/setup.bash
$ ros2 launch caddybot bringup.py
```

## build MCU
1. git clone
```
$ git clone --recursive https://github.com/bosornd/caddybot_mcu.git
$ cd caddybot_mcu
```
2. install dependencies
```
$ rosdep install --from-paths src --ignore-src --rosdistro humble -y
```
3. build
```
$ colcon build
$ source install/setup.bash
```
4. build firmware
```
$ ros2 run micro_ros_setup create_firmware_ws.sh host
$ ros2 run micro_ros_setup build_firmware.sh
```

## launch MCU
using terminal2(micro-ROS),
```
$ source install/setup.bash
$ ros2 launch caddybot_mcu mcu.py
```
using termianal3(ROS2),
publishing a Velocity topic confirms that it is delivered to MCU via micro_ros_agent.
```
$ source install/setup.bash
$ ros2 topic pub --once /velocity caddybot_msgs/msg/Velocity '{speed: 0.8, angle: 0.0}'
```

## architecture
![architecture by rqt_graph](/img/architecture.png)
