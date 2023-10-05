import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LED(Node):

    def __init__(self):
        super().__init__('led')

        self.subscription = self.create_subscription(String, '/led', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'LED={msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = LED()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()