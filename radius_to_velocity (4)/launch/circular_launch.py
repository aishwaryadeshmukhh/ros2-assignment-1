from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='radius_to_velocity',
            executable='radius_publisher',
            name='radius_publisher'
        ),
        Node(
            package='radius_to_velocity',
            executable='velocity_calculator',
            name='velocity_calculator'
        ),
        Node(
            package='radius_to_velocity',
            executable='motion_controller',
            name='motion_controller'
        ),
        Node(
            package='radius_to_velocity',
            executable='infinitylooper',
            name='infinitylooper'
        )
    ])
