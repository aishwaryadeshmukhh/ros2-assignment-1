import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RadiusPublisher(Node):
    def __init__(self):
        super().__init__('radius_publisher')
        self.publisher = self.create_publisher(Float32, 'radius', 10)
        self.timer = self.create_timer(1.0, self.publish_radius)
        self.current_radius = 1.0

    def publish_radius(self):
        radius_message = Float32()
        radius_message.data = self.current_radius
        self.publisher.publish(radius_message)
        self.get_logger().info(f'Published radius: {self.current_radius}')

def main(args=None):
    rclpy.init(args=args)
    node = RadiusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
