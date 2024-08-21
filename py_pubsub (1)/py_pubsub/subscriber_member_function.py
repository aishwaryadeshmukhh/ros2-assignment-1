import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldSubscriber(Node):
    def __init__(self):
        super().__init__('HelloWorldSubscriber')
        self.hello_message = None
        self.world_message = None
        self.create_subscription(String, 'hello', self.hello_callback, 10)
        self.create_subscription(String, 'world', self.world_callback, 10)
        self.publisher_ = self.create_publisher(String, 'helloworld', 10)

    def hello_callback(self, msg):
        self.hello_message = msg.data
        self.publish_combined_message()

    def world_callback(self, msg):
        self.world_message = msg.data
        self.publish_combined_message()

    def publish_combined_message(self):
        if self.hello_message and self.world_message:
            combined_msg = String()
            combined_msg.data = f"{self.hello_message}, {self.world_message}"
            self.publisher_.publish(combined_msg)
            self.get_logger().info('Published combined message: "%s"' % combined_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
