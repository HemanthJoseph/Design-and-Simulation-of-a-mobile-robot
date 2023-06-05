#!/usr/bin/python
# -*- coding: utf-8 -*-
        
import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' I received %s', str(data.data))

def robot_subscriber():

    rospy.init_node('listen_to_info', anonymous=True)

    #rospy.Subscriber('hey', Float64, callback) #replace topic name here ''
    rospy.Subscriber('/trolley/FR_axel_controller/command', Float64, callback)
    rospy.Subscriber('/trolley/FL_axel_controller/command', Float64, callback)
    rospy.Subscriber('/trolley/RR_wheel_controller/command', Float64, callback)
    rospy.Subscriber('/trolley/RL_wheel_controller/command', Float64, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    robot_subscriber()        
