import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPS(Node):

    def __init__(self):
        super().__init__('gps')

        self.publisher = self.create_publisher(NavSatFix, '/gps', 10)

def main(args=None):
    rclpy.init(args=args)

    node = GPS()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()