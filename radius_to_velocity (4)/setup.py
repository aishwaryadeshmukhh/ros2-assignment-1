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
        ('share/' + package_name + '/launch', ['launch/circular_launch.py']),  # Include launch files
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
            'radius_publisher = radius_to_velocity.radius_publisher:main',
            'infinitylooper = radius_to_velocity.infinitylooper:main',
            'motion_controller = radius_to_velocity.motion_controller:main',
            'velocity_calculator = radius_to_velocity.velocity_calculator:main',
        ],
    },
)
