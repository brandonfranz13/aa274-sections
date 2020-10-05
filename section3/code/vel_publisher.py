import rospy
from geometry_msgs import Twist

def publisher():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('cmd_vel', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        my_message = Twist()
        my_message.linear = (0, 0, 0)
        my_message.angular = (0, 0, 0)
        pub.publish(my_message)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass