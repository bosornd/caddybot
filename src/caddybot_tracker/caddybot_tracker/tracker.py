import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from caddybot_msgs.msg import Object
from caddybot_msgs.msg import ObjectArray
from caddybot_msgs.msg import RegionArray

class Tracker(Node):

    def __init__(self):
        super().__init__('tracker')

        self.publisher            = self.create_publisher(ObjectArray, '/objects', 10)
        self.robot_subscription   = self.create_subscription(Object, '/robot', self.robot_callback, 10)
        self.regions_subscription = self.create_subscription(RegionArray, '/regions', self.regions_callback, 10)

        self.objects = ObjectArray()

    def robot_callback(self, msg):
        self.robot = msg

    def regions_callback(self, msg):
        # Todo. trace objects by kalman filter
        
        self.publisher.publish(self.objects)

def main(args=None):
    rclpy.init(args=args)

    node = Tracker()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()