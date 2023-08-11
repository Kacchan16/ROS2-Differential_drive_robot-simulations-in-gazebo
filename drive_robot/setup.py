from setuptools import setup
import os
from glob import glob

package_name = 'drive_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('yaml/*.yaml'))
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='venkata',
    maintainer_email='venkata@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'command_node = drive_robot.command_move:main',
            'command_motion_node = drive_robot.command_motion:main'
        ],
    },
)
