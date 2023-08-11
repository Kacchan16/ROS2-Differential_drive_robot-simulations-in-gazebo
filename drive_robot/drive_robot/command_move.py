#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SendCommands(Node):
    def __init__(self):
        super().__init__("command_node")
        
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/diff_drive_base_controller/cmd_vel_unstamped", 10)
        self.timer_ = self.create_timer(1, self.send_velocity_command)

            
        self.get_logger().info("Sending commands started")


    def send_velocity_command(self):
            
            msg = Twist()
            msg.linear.x = 0.5
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x = 0.0
            msg.angular.y = 0.0
            msg.angular.z = 0.5
            self.get_logger().info("Robot is moving")

            self.cmd_vel_pub_.publish(msg)        

def main(args=None):
    rclpy.init(args=args)
    node = SendCommands()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

