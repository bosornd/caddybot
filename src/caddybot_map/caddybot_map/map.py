import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from caddybot_msgs.msg import Location
from caddybot_msgs.srv import GetZone

class map(Node):

    def __init__(self):
        super().__init__('map')

        self.service = self.create_service(GetZone, 'get_zone', self.get_zone_callback)

    def get_zone_callback(self, request, response):
        location = request.location

        # get the zone that the requested location is

        response.zone = String()
        return response


def main(args=None):
    rclpy.init(args=args)

    node = map()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()