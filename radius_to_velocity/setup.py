from setuptools import setup

package_name = 'radius_to_velocity'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/ComputeAngVel.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='maintainer',
    maintainer_email='maintainer@example.com',
    description='Description of radius_to_velocity',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'compute_ang_vel_service = radius_to_velocity.compute_ang_vel_service:main',
            'radius_publisher = radius_to_velocity.radius_publisher:main',
            'turtlebot_controller = radius_to_velocity.turtlebot_controller:main',
        ],
    },
)
