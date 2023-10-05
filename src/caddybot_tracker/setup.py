from setuptools import find_packages, setup

package_name = 'caddybot_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yong Jin, Cho',
    maintainer_email='drajin.cho@bosornd.com',
    description='Caddybot Tracker Module',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pov = caddybot_tracker.pov:main',
            'avg = caddybot_tracker.avg:main',
            'tracker = caddybot_tracker.tracker:main',
        ],
    },
)
