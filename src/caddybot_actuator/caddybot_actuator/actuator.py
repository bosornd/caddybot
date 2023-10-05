import rclpy
from rclpy.node import Node
from caddybot_msgs.msg import Velocity

class Actuator(Node):

    def __init__(self):
        super().__init__('actuator')

        self.subscription = self.create_subscription(Velocity, '/velocity', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'speed={msg.speed}, angle={msg.angle}')


def main(args=None):
    rclpy.init(args=args)

    node = Actuator()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()