#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64



def robot_publisher():
    rospy.init_node('publish_speed_to_Gazebo')
    #pub_move = rospy.Publisher('hey', Float64, queue_size=10) #replace 'hey' with topic names for move
    pub_steer_Right = rospy.Publisher('/trolley/FR_axel_controller/command', Float64, queue_size=10)
    pub_steer_Left = rospy.Publisher('/trolley/FL_axel_controller/command', Float64, queue_size=10)
    pub_move_RR = rospy.Publisher('/trolley/RR_wheel_controller/command', Float64, queue_size=10)
    pub_move_RL = rospy.Publisher('/trolley/RL_wheel_controller/command', Float64, queue_size=10)
    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        speed_right = -3
	speed_left = 3
	turn_right = 0.5
	turn_left = -0.5
        #pub_move.publish(speed)
	pub_steer_Right.publish(turn_right)
	pub_steer_Left.publish(turn_left)
        pub_move_RR.publish(speed_right)
        pub_move_RL.publish(speed_left)
        r.sleep()
	rospy.loginfo('Turn given to right wheel' + str(turn_right))
	rospy.loginfo('Turn given to left wheel' + str(turn_left))
        rospy.loginfo('Speed sent to right wheel' + str(speed_right))
	rospy.loginfo('Speed sent to left wheel' + str(speed_left))


if __name__ == '__main__':
    try:
        robot_publisher()
    except rospy.ROSInterruptException:
        pass
