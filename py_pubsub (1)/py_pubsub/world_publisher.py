import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WorldPublisher(Node):
    def __init__(self):
        super().__init__('world_publisher')
        self.publisher_ = self.create_publisher(String, 'world', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'World'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = WorldPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
