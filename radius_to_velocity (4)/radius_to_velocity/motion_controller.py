import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from radius_to_velocity.srv import ComputeAngVel

class MotionController(Node):
    def __init__(self):
        super().__init__('motion_controller')

        self.radius_subscription = self.create_subscription(            ##subscribe to /radius topic
            Float32, 'radius', self.handle_radius, 10
        )
        
        self.twist_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)         ##publish cmd_vel
        
        self.ang_vel_client = self.create_client(ComputeAngVel, 'calculate_angular_velocity')       ##create client for angvel service
        
        while not self.ang_vel_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for angular velocity service...')
        
        self.request = ComputeAngVel.Request()          ##service request

    def handle_radius(self, msg):
        self.request.radius = msg.data              ##request radius
        
        future = self.ang_vel_client.call_async(self.request)           ##call service
        future.add_done_callback(self.process_angular_velocity)
        self.get_logger().info(f'Received radius: {self.request.radius}')

    def process_angular_velocity(self, future):
        try:
            response = future.result()
            twist_message = Twist()
            twist_message.linear.x = 0.1  
            twist_message.angular.z = response.angular_velocity
            self.twist_publisher.publish(twist_message)
            self.get_logger().info(f'Sent twist message: Linear Velocity: 0.1, Angular Velocity: {response.angular_velocity}')
        except Exception as e:
            self.get_logger().error(f'Failed to call service: {e}')

def main(args=None):
    rclpy.init(args=args)
    motion_controller = MotionController()
    rclpy.spin(motion_controller)
    motion_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
