#!/usr/bin/python3 

import rospy
from geometry_msgs.msg import Twist
from getkey import getkey, keys

rospy.init_node("mykey_tele_n", anonymous=True)
pub_handle_py = rospy.Publisher("cmd_vel", Twist, queue_size=10)

twist = Twist()
x=0
z=0
loop_hz = rospy.Rate(20)
msg="""
-----------------------------
Press 'w' -> move forward
      's' -> move backward
      'a' -> Turn left
      'd' -> Turn right
-----------------------------
      w
   a  s  d
-----------------------------

"""
print(msg)
while not rospy.is_shutdown():
    key = getkey()
    if key == 'w':
        if twist.linear.x == -0.5:
            twist.linear.x  = 0.0 
            x=0.0
        else:
            twist.linear.x  = 0.5 
            x=0.2
            twist.angular.z = 0.0

    elif key == 's':
        if twist.linear.x == 0.5:
            twist.linear.x = 0.0
            x = 0.0
        else:
            twist.linear.x = -0.5 
            twist.angular.z = 0.0

    elif key == 'a':
        twist.linear.x = x
        twist.angular.z = 1
    elif key == 'd':
        twist.linear.x = x
        twist.angular.z = -1
    else:
        twist.linear.x = 0.0
        twist.angular.z = 0.0

    pub_handle_py.publish(twist)
    loop_hz.sleep()