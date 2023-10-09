import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import Point

import utm

class UTM(Node):

    def __init__(self):
        super().__init__('utm')

        self.publisher = self.create_publisher(Point, '/position', 10)
        self.subscription = self.create_subscription(NavSatFix, '/gps', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'latitude={msg.latitude}, longitude={msg.longitude}, altitude={msg.altitude}')
        xy = utm.from_latlon(msg.latitude, msg.longitude)

        out = Point()
        out.x = xy[0]
        out.y = xy[1]
        out.z = 0

        self.publisher.publish(out)

def main(args=None):
    rclpy.init(args=args)

    node = UTM()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()