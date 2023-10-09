from setuptools import find_packages, setup

package_name = 'caddybot_gps'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'sparkfun-ublox-gps', 'utm'],
    zip_safe=True,
    maintainer='Yong Jin, Cho',
    maintainer_email='drajin.cho@bosornd.com',
    description='Caddybot GPS Module',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fake_gps = caddybot_gps.fake_gps:main',
            'gps = caddybot_gps.gps:main',
            'utm = caddybot_gps.utm:main',
        ],
    },
)
