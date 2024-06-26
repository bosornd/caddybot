from setuptools import find_packages, setup

package_name = 'caddybot_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yong Jin, Cho',
    maintainer_email='drajin.cho@bosornd.com',
    description='Caddybot Tracker Module',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'segmenter = caddybot_tracker.segmenter:main',
            'tracker = caddybot_tracker.tracker:main',
        ],
    },
)
