import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

import serial
from ublox_gps import UbloxGps

class GPS(Node):

    def __init__(self):
        super().__init__('gps')

        self.declare_parameter('gps', '/dev/pts/0')
        self.device = self.get_parameter('gps').get_parameter_value().string_value

        self.publisher = self.create_publisher(NavSatFix, '/gps', 10)

        self.port = serial.Serial(self.device, baudrate=38400, timeout=1)
        self.gps = UbloxGps(self.port)

    def run(self):
        try: 
            while True:
                try:
                    geo = self.gps.geo_coords()
                    cov = self.gps.geo_cov()

                    self.get_logger().info(f'latitude={geo.lat}, longitude={geo.lon}')

                    out = NavSatFix()
                    out.longitude = geo.lon
                    out.latitude = geo.lat
                    out.altitude = 0.001 * float(geo.height)
                    out.position_covariance = [cov.posCovEE, cov.posCovNE, cov.posCovED, cov.posCovNE, cov.posCovNN, cov.posCovND, cov.posCovED, cov.posCovND, cov.posCovDD]
                    out.position_covariance_type = 3

                    self.publisher.publish(out)
                except (ValueError, IOError) as err:
                    print(err)
        finally:
            port.close()

def main(args=None):
    rclpy.init(args=args)

    node = GPS()
    node.run()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()