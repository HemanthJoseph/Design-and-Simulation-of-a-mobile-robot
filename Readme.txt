This project is made using ROS 1

Firstly make sure you have ROS installed in your system. If not, visit http://wiki.ros.org/ROS/Installation and install ROS
If you already have ROS installed in your system, make sure to setup the sources list and setup your keys. Visit http://wiki.ros.org/noetic/Installation/Ubuntu (Incase you're using ROS Noetic)

Install the necessary controllers packages using the following command, 
sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers 
(change the version of ROS as per your installation)

Unzip the provided Zip file to the location of your choice and then copy the "trolley" package into the src folder inside your catkin workspace. Steps to create a catkin workspace is mentioned here http://wiki.ros.org/catkin/Tutorials/create_a_workspace

After placing it into the src folder, navigate to the catkin workspace in your terminal

In the terminal, build the catkin workspace using the command, 
catkin_make
Unless you are using a previously used workspace, it will create two new folders, "devel" and "build" inside the workspace folder.

Now, after you build it, from the workspace folder in the terminal source your setup file using the command,
source devel/setup.bash

After sourcing the workspace, run the following command in the terminal from the workspace folder,
roslaunch trolley template_launch.launch
Here "trolley" is the name of our package. Running this command will launch the robot in the Gazebo simulator in a world as provided by the project resource

Now launch RViz, by opening a new terminal window/tab, and enter the following command, 
rviz

In a new terminal window/tab, navigate to the folder which contains the python scripts for teleop by using the following command,
cd src/trolley/src

we first need to declare the python script to be an executable in ROS
Enter the following command in the terminal from the src folder,
sudo chmod +x teleop_template.py
This will ask for your password, type in and enter your password and it will convert your file into an executable.

Since the robot is already launched in Gazebo, enter the following command in the terminal,
python3 teleop_template.py
If that doesn't work, it is because of the difference between the python versions, in terminal enter the following command,
python teleop_template.py

Now the control keys are opened in the terminal using the following keys, the robot can be moved around in the environment
i - move forwards
, - move backwards
u - move left
o - move right
j - turn left
l - turn right
k - force stop
You can use the keys as required to teleoperate the robot in the Gazebo environment

After the necessary tasks are done, press 'Ctrl + C' in all the active terminals to terminate the running tasks

Next we make the Robot move in an empty world by receiving command from the publisher

In the terimal, from the main workspace folder run the following command,
roslaunch trolley empty_launch.launch

This will launch the robot in the empty world

Now in the previously used terminal tab (where we have the python scripts) we declare the publisher and the subscriber programs to be a ROS executable by running the following command,
sudo chmod +x robot_publisher.py

Now make the subscriber program an executable by the following command,
sudo chmod +x robot_subscriber.py
After declaring both the subscriber and the publisher as executables, we run the files

In the same terminal run the following command,
python3 robot_publisher.py
This will start to publish the movement commands which are subscribed by the robot and it moves in Gazebo

In a new terminal from the same folder containing python scripts, run the following command,
python3 robot_subscriber.py
This will start a subscriber node and this will print the messages (on the terminal) being published to respective topics by the publisher

You can notice that the robot is turning in circular path in Gazebo
After a few moments, press 'Ctrl + C' in all terminals to terminate the running tasks

Thus the project is successfully executed
