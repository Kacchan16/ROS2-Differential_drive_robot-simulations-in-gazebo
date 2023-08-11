import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('drive_robot'),
        'config',
        'commands.yaml'
    )

    my_node = Node(
        package="drive_robot",
        name="command_motion_node",
        executable="command_motion_node",
        parameters=[config]
    )

    ld.add_action(my_node)
    return ld