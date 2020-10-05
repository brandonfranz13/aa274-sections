import rospy
from geometry_msgs import Twist

def callback(cmd_vel):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", cmd_vel)


def subscriber():
    rospy.init_node('odom_sub', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback(cmd_vel))
    rospy.spin()


if __name__ == '__main__':
    subscriber()