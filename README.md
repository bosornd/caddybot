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
$ pip install shapely
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
$ source install/setup.bash
```

## launch
```
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
$ source install/setup.bash
```

## launch MCU
```
$ ros2 launch caddybot_mcu mcu.py
```
publishing a Velocity topic confirms that it is delivered to MCU through micro_ros_agent.
```
$ ros2 topic pub --once /velocity caddybot_msgs/msg/Velocity '{speed: 0.8, angle: 0.0}'
```

## architecture
![architecture by rqt_graph](/img/architecture.png)
![architecture by rqt_graph](/img/architecture2.png)

## test micro-ros-agent
1. in terminal 1,
```
$ ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```
![micro_ros_agent starting](/img/micro_ros_agent1.png)

2. in terminal 2,
```
$ export RMW_IMPLEMENTATION=rmw_microxrcedds
$ ros2 run caddybot_mcu mcu
```
![MCU starting](/img/micro_ros_agent2.png)
![micro_ros_agent connected](/img/micro_ros_agent3.png)

3. in terminal 3,
```
$ ros2 topic pub --once /velocity caddybot_msgs/msg/Velocity '{speed: 0.8, angle: 0.0}'
```
![topic published](/img/micro_ros_agent4.png)
![MCU received](/img/micro_ros_agent5.png)

