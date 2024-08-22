import rclpy
from rclpy.node import Node
from radius_to_velocity import ComputeAngVel

class VelocityCalculator(Node):
    def __init__(self):
        super().__init__('velocity_calculator')
        self.service = self.create_service(ComputeAngVel, 'calculate_angular_velocity', self.handle_velocity_request)

    def handle_velocity_request(self, request, response):
        default_linear_velocity = 0.1
        radius = request.radius
        if radius != 0:
            computed_angular_velocity = default_linear_velocity / radius
        else:
            computed_angular_velocity = 0.0
        response.angular_velocity = computed_angular_velocity
        self.get_logger().info(f'Radius received: {radius}, Computed angular velocity: {computed_angular_velocity}')
        return response

def main(args=None):
    rclpy.init(args=args)
    velocity_calculator = VelocityCalculator()
    rclpy.spin(velocity_calculator)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
