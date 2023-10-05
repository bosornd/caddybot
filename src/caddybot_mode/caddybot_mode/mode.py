import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Mode(Node):

    def __init__(self):
        super().__init__('mode')

        self.publisher = self.create_publisher(String, '/mode', 10)

def main(args=None):
    rclpy.init(args=args)

    node = Mode()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()