

# Differential drive robot simulations in Gazebo, ROS2

Welcome to the readme file of this project. In this project, my goal is to setting up a ROS2 environment for simulations of Differential drive robot in Gazebo and give publlisher command to move the Differential drive robot in alternating cyclic commands through yaml file. And I created launch files for this publlisher command and updated setup.py for execution.


## Description

I made this project in ROS2 - galactic. After creating your Linux, first start setting the environment by followimg ROS2 wiki documentation


https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html

## Compile from Source

I followed these following commands in order to setup ROS2 environment.

```bash
  locale
  sudo apt update && sudo apt install locales
  sudo locale-gen en_US en_US.UTF-8
  sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
  export LANG=en_US.UTF-8

  locale  # verify settings

```
You will need to add the ROS 2 apt repository to your system.
```bash
  sudo apt install software-properties-common
  sudo add-apt-repository universe

```
Now add the ROS 2 GPG key with apt.
```bash
  sudo apt update && sudo apt install curl
  sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Then add the repository to your sources list.
```bash
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
## Install Ros2 packages

```bash
  sudo apt update

  sudo apt upgrade

  sudo apt install ros-galactic-desktop
```
after Installation of galactic desktop verison, we can setup the environment by souring

```bash
 source /opt/ros/galactic/setup.bash
```
## Intsall remaining required packages
These are the commands for installing of packages required for our robot

    sudo apt install ros-galactic-xacro
    sudo apt install ros-galactic-ros2-control
    sudo apt install ros-galactic-ros2-controllers
    sudo apt install ros-galactic-gazebo-ros-pkgs
    sudo apt install ros-galactic-gazebo-ros2-control



After installing all the packages till now point, our environment is ready, for working of the differential drive robot. Now  we can create a workspace and python package.

```bash
 mkdir -p ~/ros2_ws/src
 cd ~/ros2_ws
 colcon build

 cd ros_ws/src
     ros2 pkg create drive_robot --build-type ament_python --dependencies std_msgs rclpy geometry_msgs
 cd ..
 colcon build
```

https://github.com/ros-controls/gz_ros2_control

for ros2_controls, I used this one, While installing mention your ros2 version and make -b

```bash
 cd ros_ws/src
 git clone -b galactic https://github.com/ros-controls/gz_ros2_control
```
after sourcing the workspace, use this command everytime.
```bash
  source install/setup.bash
```
After installing all the necessary packages, try launching differential drive robot in gazebo, by typing 
```bash
  ros2 launch ign_ros2_control_demos diff_drive_example.launch.py 
```
Then to give commands for our differential drive robot, we have to create a node. To give the alternating cyclic commands for our robot, and then made one more new python file and pass these commands through the file.

```bash
  cd ros2_ws/src/drive_robot/drive_robot
  touch command_motion.py
  chmod +x command_motion.py
```
Then write the commands in .yaml file
```bash
  cd ros2_ws/src/drive_robot
  mkdir config
  cd config
  touch commands.yaml
```
Then we can try the ros2 launch file for robot spawning in gazebo and run ros2 run command_move.py for the movement of robot.

After looking everything is good, made one launch file for the commands of the robot.

```bash
  cd ros2_ws/src/drive_robot
  mkdir launch
  cd launch
  touch robot_motion.launch.py
  chmod +x robot_motion.launch.py
```
Then open the two terminals and source the terminals, and type the following commands in two terminals.
```bash
  ros2 launch ign_ros2_control_demos diff_drive_example.launch.py 
  ros2 launch drive_robot robot_motion.launch.py
```
Then you can see our robot in gazebo environment and moving in alternating cyclic commands.



