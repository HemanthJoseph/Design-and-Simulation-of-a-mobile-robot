# Modelling a Robot and controlling it in Gazebo and ROS
The aim of this project is understand how to do the following
1. Design a robot car using Solidworks.
2. Convert it to a URDF (Universal Robot Description Format).
3. Apply inertial physics to it, add a LIDAR sensor, controllers for motion control
4. Create a ROS package containing the XACRO files ready for launch
5. Write the appropriate launch files and run the robot in a simulated Gazebo world and to also control it through teleop

## Dependencies
This project is made using ROS 1

1. Firstly make sure you have ROS installed in your system. If not, visit http://wiki.ros.org/ROS/Installation and install ROS.
If you already have ROS installed in your system, make sure to setup the sources list and setup your keys. Visit http://wiki.ros.org/noetic/Installation/Ubuntu (Incase you're using ROS Noetic)

2. Update your linux environment
```
sudo apt update
```
```
sudo apt upgrade
```
3. Install the necessary controllers packages using the following command. (change the version of ROS as per your installation)

```
sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers
```


## Usage

### Launching the robot in a Gazebo world and teleoperating it.

1. Unzip the provided Zip file to the location of your choice and then copy the "trolley" package into the src folder inside your catkin workspace. Steps to create a catkin workspace is mentioned here http://wiki.ros.org/catkin/Tutorials/create_a_workspace

2. After placing it into the src folder, navigate to the catkin workspace in your terminal

3. In the terminal, build the catkin workspace using the below command. Unless you are using a previously used workspace, it will create two new folders, "devel" and "build" inside the workspace folder.
```
catkin_make
```


4. Now, after you build it, from the workspace folder in the terminal source your setup file using the command
```
source devel/setup.bash
```

5. After sourcing the workspace, run the following command in the terminal from the workspace folder. Here "trolley" is the name of our package. Running this command will launch the robot in the Gazebo simulator in a world as provided by the project resource.
```
roslaunch trolley template_launch.launch
```

6. Now launch RViz, by opening a new terminal window/tab, and enter the following command
```
rviz
```

7. In a new terminal window/tab, navigate to the folder which contains the python scripts for teleop by using the following command
```
cd src/trolley/src
```

8. we first need to declare the python script to be an executable in ROS
Enter the following command in the terminal from the src folder. This will ask for your password, type in and enter your password and it will convert your file into an executable.
```
sudo chmod +x teleop_template.py
```

9. Since the robot is already launched in Gazebo, enter the following command in the terminal. (If that doesn't work, it is because of the difference between the python versions, in terminal enter the following command,
python teleop_template.py)
```
python3 teleop_template.py
```


10. Now the control keys are opened in the terminal using the following keys, the robot can be moved around in the environment. You can use the keys as required to teleoperate the robot in the Gazebo environment.
```
i - move forwards
, - move backwards
u - move left
o - move right
j - turn left
l - turn right
k - force stop
```
11. After the necessary tasks are done, press 'Ctrl + C' in all the active terminals to terminate the running tasks

### Launching the robot in an empty world and giving it pre-programmed motions through a publisher and Subscriber


Next we make the Robot move in an empty world by receiving command from the publisher.

1. In the terimal, from the main workspace folder run the following command. This will launch the robot in the empty world.
```
roslaunch trolley empty_launch.launch
```

2. Now in the previously used terminal tab (where we have the python scripts) we declare the publisher and the subscriber programs to be a ROS executable by running the following command,
```
sudo chmod +x robot_publisher.py
```

3. Now make the subscriber program an executable by the following command. After declaring both the subscriber and the publisher as executables, we run the files.
```
sudo chmod +x robot_subscriber.py
```


4. In the same terminal run the following command. This will start to publish the movement commands which are subscribed by the robot and it moves in Gazebo.
```
python3 robot_publisher.py
```


7. In a new terminal from the same folder containing python scripts, run the following command. This will start a subscriber node and this will print the messages (on the terminal) being published to respective topics by the publisher.
```
python3 robot_subscriber.py
```


You can notice that the robot is turning in circular path in Gazebo
After a few moments, press 'Ctrl + C' in all terminals to terminate the running tasks

Thus the project is successfully executed
