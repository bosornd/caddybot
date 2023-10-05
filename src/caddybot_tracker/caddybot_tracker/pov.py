import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LiDARFilter(Node):

    def __init__(self):
        super().__init__('pov')

        self.declare_parameter('front_angle', 90)       # 90 degree
        self.declare_parameter('window_size', 180)      # 180 degree

        self.front_angle = self.get_parameter('front_angle').get_parameter_value().integer_value
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

        num_ranges = len(msg.ranges)
        start = int((self.front_angle - self.window_size / 2) * 360 / num_ranges)
        end = int((self.front_angle + self.window_size / 2) * 360 / num_ranges)

        out.ranges = msg.ranges[start:] if start < 0 else []
        out.ranges.extend(msg.ranges[0 if start < 0 else start:end + 1 if end < num_ranges else num_ranges])
        out.ranges.extend(msg.ranges[:end - num_ranges + 1] if end > num_ranges else [])

        out.angle_max = out.angle_increment * len(out.ranges) / 2
        out.angle_min = -out.angle_max

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