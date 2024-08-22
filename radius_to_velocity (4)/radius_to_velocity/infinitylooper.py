
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class InfinityLooper(Node):

    def __init__(self):
        super().__init__('infinity_looper')

        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)       ##publish vel commands

        self.timer = self.create_timer(0.1, self.execute_loop)              ##call the loop every 0.1 s

        self.loop_time = 30  ##complete half of figure 8
        self.initial_time = self.get_clock().now().to_msg().sec

    def execute_loop(self):
        current_time = self.get_clock().now().to_msg().sec
        elapsed_time = current_time - self.initial_time
        velocity_command = Twist()
        velocity_command.linear.x = 0.1

        if elapsed_time < self.loop_time:                               ##calculate the angular velocity - logic yt
            velocity_command.angular.z = 2 * math.pi / self.loop_time
        elif elapsed_time < 2 * self.loop_time:
            velocity_command.angular.z = -2 * math.pi / self.loop_time
        else:
            self.initial_time = current_time  ##resettimer for loop to continue

        self.cmd_vel_publisher.publish(velocity_command)            ##publish velocity cmd

def main(args=None):
    rclpy.init(args=args)
    looper = InfinityLooper()
    rclpy.spin(looper)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
