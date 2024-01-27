import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from caddybot_msgs.msg import RegionArray

class Segmenter(Node):

    def __init__(self):
        super().__init__('segmenter')

        self.publisher    = self.create_publisher(RegionArray, '/regions', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.callback, 10)

    def callback(self, msg):
        regions = RegionArray()

        # ToDo
        # segment regions from scan.angle_min to scan.angle_max based on range similarity

        self.publisher.publish(regions)

def main(args=None):
    rclpy.init(args=args)

    node = Segmenter()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()