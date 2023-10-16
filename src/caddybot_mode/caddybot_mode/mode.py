import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from caddybot_msgs.srv import GetMode

class Mode(Node):

    def __init__(self):
        super().__init__('mode')

        self.publisher = self.create_publisher(String, '/mode', 10)
        self.service = self.create_service(GetMode, 'get_mode', self.get_mode_callback)

        self.mode = "Undefined"

    def get_mode_callback(self, request, response):
        response.mode = String()
        response.mode.data = self.mode

        return response


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