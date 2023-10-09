import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point
from caddybot_msgs.msg import Velocity, GetZone

import math

class ZoneController(Node):

    def __init__(self):
        super().__init__('zone_controller')

        self.sound_publisher = self.create_publisher(String, '/sound', 10)
        self.velocity_publisher = self.create_publisher(Velocity, '/velocity/output', 10)
        self.velocity_subscription = self.create_subscription(Velocity, '/velocity/input', self.velocity_callback, 10)
        self.zone_subscription = self.create_subscription(String, '/zone', self.zone_callback, 10)
        self.position_subscription = self.create_subscription(Point, '/position', self.position_callback, 10)

        self.zone_client = self.create_client(GetZone, 'get_zone')
        while not self.zone_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def get_zone(self, location):
        request = GetZone.Request()

        request.location.x = location.x
        request.location.y = location.y
        request.location.z = location.z

        future = self.zone_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        return future.result().zone

    def check_restricted_zone(self, zone):
        ristricted_zone = [ "hole", "green", "bunker", "hazard" ]
        try:
            ristricted_zone.index(zone)
        except:
            return False

        return True

    def velocity_callback(self, msg):
        location.x = self.location.x + msg.speed * math.sin(msg.angle)
        location.y = self.location.y + msg.speed * math.cos(msg.angle)
        location.z = self.location.z

        zone = self.get_zone(location)
        if self.check_restricted_zone(zone):
            msg.speed = 0
            msg.angle = 0

            self.sound_publisher.publish("hazard_stop")

        self.velocity_publisher.publish(msg)

    def zone_callback(self, msg):
        if self.zone != msg.data:
            self.zone = msg.data

            if self.zone == "cart_path":
                self.sound_publisher.publish("cart_path")

    def position_callback(self, msg):
        self.location.x = msg.x
        self.location.y = msg.y
        self.location.z = msg.z

def main(args=None):
    rclpy.init(args=args)

    node = ZoneController()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()