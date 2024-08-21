from setuptools import find_packages, setup

package_name = 'py_srvcli'

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
    maintainer='Aishwarya',
    maintainer_email='aishu6167@gmail.com',
    description='ROS2 SPAWN TURTLE SERVICE AND CLIENT ',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_turtle_service = py_srvcli.spawn_turtle_service:main',
            'spawn_turtle_client = py_srvcli.spawn_turtle_client:main',
        ],
    },
)
