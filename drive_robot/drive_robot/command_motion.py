#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import os
import yaml

class SendCommands(Node):
    def __init__(self):
        super().__init__("command_motion_node")
        
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/diff_drive_base_controller/cmd_vel_unstamped", 10)
        self.timer_ = self.create_timer(2, self.send_velocity_command)

        self.commands = self.load_commands_from_yaml()
        #print("Loaded commands:", self.commands)
        
        self.commands_index = 0        
        self.get_logger().info("Sending commands started")

    
    def load_commands_from_yaml(self):
        yaml_file_path = os.path.expanduser('~/ros2_ws/src/drive_robot/config/commands.yaml')
        print(f"Loading YAML file from: {yaml_file_path}")
        
        with open(yaml_file_path, 'r') as file:
            commands_data = yaml.safe_load(file)
        
        print(f"Loaded data: {commands_data}")
        
        return commands_data.get('commands', []) 

    def send_velocity_command(self):
        if self.commands:
            cmd = self.commands[self.commands_index]
            self.commands_index = (self.commands_index + 1) % len(self.commands)
            
            msg = Twist()
            print("Robot is moving ")
            self.get_logger().info("Robot is moving")

            msg.linear.x = cmd['linear']['x']
            msg.linear.y = cmd['linear']['y']
            msg.linear.z = cmd['linear']['z']
            msg.angular.x = cmd['angular']['x']
            msg.angular.y = cmd['angular']['y']
            msg.angular.z = cmd['angular']['z']


            if msg.linear.x == 0.0 and msg.angular.z == 0.0:
                self.get_logger().info("Stopping the robot")
                self.cmd_vel_pub_.publish(msg)  
                self.timer_.cancel()  
                return       

            self.cmd_vel_pub_.publish(msg)     


def main(args=None):
    rclpy.init(args=args)
    node = SendCommands()
    
    try:
        print("command motion node is starting ...")
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()






    

    

