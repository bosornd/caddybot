import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import os
import pygame

DIRECTORY = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]) + "/sounds/"
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

class SoundManager(Node):

    def __init__(self):
        super().__init__('sound_manager')

        pygame.init()

        self.subscription = self.create_subscription(String, '/sound', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'sound={msg.data}')
        pygame.mixer.Sound(DIRECTORY + msg.data + ".mp3").play()

def main(args=None):
    rclpy.init(args=args)

    node = SoundManager()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()