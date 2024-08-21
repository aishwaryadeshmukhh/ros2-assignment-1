import sys
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist

class SpawnTurtleClient(Node):
    def __init__(self):
        super().__init__('spawn_turtle_client')
        self.cli = self.create_client(Spawn, 'spawn')
        self.publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)

        self.send_request() ##once client is ready for spawn and publisher for velocity. spawn the turtle

    def send_request(self):
        req = Spawn.Request()
        req.x = 3.0
        req.y = 3.0
        req.theta = 0.0
        req.name = 'turtle2'

        ##debugging using gpt - turtle getting spawned later ##doubt
        # Send the spawn request and wait for it to complete
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)

        # After confirming the turtle is spawned, send velocity commands
        if future.result() is not None:
            self.get_logger().info('Turtle2 spawned successfully')
            # Ensure the publisher is ready before sending velocity
            self.send_velocity()
        else:
            self.get_logger().error('Failed to spawn turtle2')

        """self.cli.call_async(req)    ##calling asynchronously and waiting for the request to complete
        rclpy.spin_once(self)  ##first process the request before moving aheadl."""

        self.send_velocity()

    def send_velocity(self):
        vx = float(sys.argv[1])
        vy = float(sys.argv[2])

        twist = Twist()             ##ceate velocity by taking arguments from cmd to turtle
        twist.linear.x = vx
        twist.linear.y = vy
        twist.angular.z = 0.0

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = SpawnTurtleClient()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
