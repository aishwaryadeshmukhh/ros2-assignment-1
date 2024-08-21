import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from example_interfaces.srv import AddTwoInts

class TurtleBotControlService(Node):

    def __init__(self):
        super().__init__('turtlebot_control_service')
        
        self.srv = self.create_service(AddTwoInts, 'control_turtlebot', self.control_turtle_callback)   ##callback corresponds to rcply.spin_once
        
        self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)       ##publisher to send cmd_vel
        
        self.get_logger().info('TurtleBot control service is ready!')

    def control_turtle_callback(self, request, response):
        vx = request.a              ##get velocity requests
        vy = request.b

        twist = Twist()             ##publish basic twist message
        twist.linear.x = vx
        twist.linear.y = vy
        twist.angular.z = 0.0

        self.publisher.publish(twist)
        
        self.get_logger().info(f'Moving TurtleBot with vx: {vx}, vy: {vy}')

        response.sum = 1        ##addtwoints instance-sum that is expected to be received by client, 1 is placeholder value
        return response

def main(args=None):
    rclpy.init(args=args)
    node = TurtleBotControlService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
