from setuptools import find_packages, setup
import os

package_name = 'caddybot_zone'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/map', [os.path.join("map", f) for f in os.listdir("map")]),
    ],
    install_requires=['setuptools', 'shapely'],
    zip_safe=True,
    maintainer='Yong Jin, Cho',
    maintainer_email='drajin.cho@bosornd.com',
    description='Caddybot Zone Module',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zone = caddybot_zone.zone:main',
            'zone_controller = caddybot_zone.zone_controller:main',
        ],
    },
)
