import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point
from caddybot_msgs.msg import GetZone

import os
import json
import shapely.geometry as sg

MAP_DIRECTORY = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]) + "/maps/"

from dataclasses import dataclass

@dataclass
class Zone:
    id: int
    category: str
    polygon: sg.polygon.Polygon

class Map(Node):

    def __init__(self):
        super().__init__('zone')

        self.declare_parameter('map', 'sample')      # 10 points
        self.map_filename = self.get_parameter('map').get_parameter_value().string_value

        self.load_map()

        self.publisher = self.create_publisher(String, '/zone', 10)
        self.subscription = self.create_subscription(Point, '/position', self.callback, 10)
        self.service = self.create_service(GetZone, 'get_zone', self.get_zone_callback)

    def load_map(self):
        with open(MAP_DIRECTORY + self.map_filename + ".json") as j:
            json_object = json.load(j)

        self.map = []
        for zone in json_object["zones"]:
            self.map.append(Zone(id=zone["id"], category=zone["category"], polygon=g.polygon.Polygon(zone["polygon"])))

    def get_zone(self, location):
        point = sg.Point([location.x, location.y])
        for zone in self.map:
            if zone.polygon.contains(point):
                return zone.category
        return "Undefined"

    def callback(self, msg):
        self.get_logger().info(f'position=({msg.x}, {msg.y}, {msg.z})')

        out = String()
        self.publisher.publish(out)

    def get_zone_callback(self, request, response):
        location = request.location
        self.get_logger().info(f'get_zone from position=({location.x}, {location.y}, {location.z})')
        # response.zone.data

        return response

def main(args=None):
    rclpy.init(args=args)

    node = Map()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()