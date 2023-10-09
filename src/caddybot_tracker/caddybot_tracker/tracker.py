import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from caddybot_msgs.msg import Velocity

class LiDARFilter(Node):

    def __init__(self):
        super().__init__('tracker')

        self.declare_parameter('max_distance', 5.0)      # 5.0m
        self.declare_parameter('min_distance', 2.0)      # 2.0m, approaching till min_distance
        self.declare_parameter('max_speed', 1.0)         # 1.0m/s

        self.max_distance = self.get_parameter('max_distance').get_parameter_value().float_value
        self.min_distance = self.get_parameter('min_distance').get_parameter_value().float_value

        self.velocity_publisher = self.create_publisher(Velocity, '/velocity', 10)
        self.sound_publisher = self.create_publisher(String, '/sound', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.callback, 10)

        self.tracking = False


    def callback(self, msg):
        scan = msg.ranges
        center = int(len(scan) / 2);

        min_distance = scan[center]

        left = center
        distance = scan[center]
        while left > 0 and abs(scan[left - 1] - distance) < 0.5:
            left -= 1
            distance = scan[left]
            if distance < min_distance:
                min_distance = distance

        right = center
        distance = scan[center]
        while right < len(scan) and abs(scan[right + 1] - distance) < 0.5:
            right += 1
            distance = scan[right]
            if distance < min_distance:
                min_distance = distance

        if not self.tracking and min_distance < self.max_distance:
            self.tracking = True
            self.sound_publisher.publish("tracker_start")

        if self.tracking and min_distance > self.max_distance:
            self.tracking = False
            self.sound_publisher.publish("tracker_lost")
            min_distance = 0
            left = right

        actuator = Actuator()
        actuator.angle = ((left + right) / 2 - center) * mgs.angle_increment
        actuator.speed = min(max_speed, (min_distance - self.min_distance) if min_distance > self.min_distance else 0)
        
        self.velocity_publisher.publish(actuator)

def main(args=None):
    rclpy.init(args=args)

    node = LiDARFilter()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()