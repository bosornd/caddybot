import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LiDAR(Node):

    def __init__(self):
        super().__init__('lidar')

        self.publisher = self.create_publisher(LaserScan, '/scan', 10)

def main(args=None):
    rclpy.init(args=args)

    node = LiDAR()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()