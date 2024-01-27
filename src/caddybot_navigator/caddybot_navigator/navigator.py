import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from caddybot_msgs.msg import Object
from caddybot_msgs.msg import ObjectArray
from caddybot_msgs.msg import Velocity
from caddybot_msgs.srv import GetZone

class Navigator(Node):

    def __init__(self):
        super().__init__('navigator')

        self.velocity_publisher   = self.create_publisher(Velocity, '/velocity', 10)
        self.sound_publisher      = self.create_publisher(String, '/sound', 10)
        self.led_publisher        = self.create_publisher(String, '/led', 10)
        self.robot_subscription   = self.create_subscription(Object, '/robot', self.robot_callback, 10)
        self.objects_subscription = self.create_subscription(ObjectArray, '/objects', self.objects_callback, 10)

        self.get_zone_client      = self.create_client(GetZone, 'get_zone')
        while not self.get_zone_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.user = None

    def get_zone(self, x, y):
        req = GetZone.Request()
        req.location.x = x
        req.location.y = y

        self.future = self.get_zone_client.call_async(req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

    def robot_callback(self, msg):
        self.robot = msg

    def setup_follower(self):
        # ToDo
        # if there is an object within 1 meter, it is recognized as user
        self.robot = self.objects[0]

        # when starting to follow user
        msg = String()
        msg.data = 'track_started'
        self.sound_publisher.publish(msg)
        self.led_publisher.publish(msg)

    def follow_user(self):
        # ToDo
        # adjust the velocity according to the distance from the user
        velocity = Velocity()
        velocity = self.robot.velocity

        # in case of missing the user
        if self.user == None:
            msg = String()
            msg.data = 'track_stopped'
            self.sound_publisher.publish(msg)
            self.led_publisher.publish(msg)
        else:
            self.velocity_publisher.publish(velocity)

    def objects_callback(self, msg):
        self.objects = msg

        if self.user == None:
            setup_follower()
        else:
            follow_user()

def main(args=None):
    rclpy.init(args=args)

    node = Navigator()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()