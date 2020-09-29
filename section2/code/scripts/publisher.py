#!/usr/bin/env python

import rospy
from aa274_s2.msg import MyMessage

def publisher():
    pub = rospy.Publisher('my_topic', MyMessage, queue_size=10) #Name the topic, choose message to publish, and define queue size
    rospy.init_node('my_node', anonymous=True) #initialization
    rate = rospy.Rate(1) #Set message rate based on ros clock
    while not rospy.is_shutdown(): #publish message while node is not shutdown
        my_message = MyMessage()
        pub.publish(my_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
