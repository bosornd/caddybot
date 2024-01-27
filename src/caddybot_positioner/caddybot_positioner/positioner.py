import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from caddybot_msgs.msg import Location
from caddybot_msgs.msg import Object

import math

class Positioner(Node):

    def __init__(self):
        super().__init__('positioner')

        self.publisher             = self.create_publisher(Object, '/robot', 10)
        self.location_subscription = self.create_subscription(Location, '/location', self.location_callback, 10)
        self.imu_subscription      = self.create_subscription(Imu, '/imu', self.imu_callback, 10)
        self.odometry_subscription = self.create_subscription(Odometry, '/odometry', self.odometry_callback, 10)

        self.robot = None

    def imu_callback(self, msg):
        self.imu = msg

    def odometry_callback(self, msg):
        self.odometry = msg

    def init_robot(self):
        self.robot = Object()

        self.robot.location = self.gps
        self.robot.velocity.speed = 0
        self.robot.velocity.angle = 0

    def update_robot(self):
        # Todo. trace robot by kalman filter
        # simple update
        self.robot.velocity.speed = 10 * math.dist([self.robot.loation.x, self.robot.location.y], [self.gps.x, self.gps.y])
        self.robot.velocity.angle = math.atan2(self.gps.y - self.robot.location.y, self.gps.x - self.robot.location.x) - self.robot.velocity.angle
        self.robot.location = self.gps

    def location_callback(self, msg):
        self.gps = msg

        if self.robot == None:
            self.init_robot()
        else:
            self.update_robot()
        
        self.publisher.publish(self.robot)

def main(args=None):
    rclpy.init(args=args)

    node = Positioner()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()