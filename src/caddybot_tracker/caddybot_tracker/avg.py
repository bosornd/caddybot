import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy

class LiDARFilter(Node):

    def __init__(self):
        super().__init__('avg')

        self.declare_parameter('window_size', 10)      # 10 points
        self.window_size = self.get_parameter('window_size').get_parameter_value().integer_value

        self.publisher = self.create_publisher(LaserScan, '/scan_out', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan_in', self.callback, 10)

    def callback(self, msg):
        out = LaserScan()
        out.header = msg.header
        out.scan_time = msg.scan_time
        out.time_increment = msg.time_increment
        out.range_min = msg.range_min
        out.range_max = msg.range_max
        out.angle_increment = msg.angle_increment

        out.angle_max = msg.angle_max
        out.angle_min = msg.angle_min

        delta = int(self.window_size / 2)
        out.ranges = msg.ranges[:delta]
        out.ranges.extend([numpy.mean(msg.ranges[i - delta:i + delta + 1]) for i in range(delta, len(msg.ranges))])

        self.publisher.publish(out)

def main(args=None):
    rclpy.init(args=args)

    node = LiDARFilter()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()