#!/usr/bin/env python
import rospy
import cv2
import numpy as np
import time
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose

bot1 = Pose()
bot2 = Pose()
bot3 = Pose()
bot4 = Pose()

def bp1(msg):
    global bot1
    bot1 = msg

def bp2(msg):
    global bot2
    bot2  = msg

def bp3(msg):
    global bot3
    bot3  = msg

def bp4(msg):
    global bot4
    bot4  = msg

def run():
    global bot1
    global bot2
    global bot3
    global bot4
    rate = rospy.Rate(20)
    xo1 = 0
    yo1 = 0
    theta_old1 = 0
    tw1 = Twist()
    xo2 = 0
    yo2 = 0
    theta_old2 = 0
    tw2 = Twist()
    xo3 = 0
    yo3 = 0
    theta_old3 = 0
    tw3 = Twist()
    xo4 = 0
    yo4 = 0
    theta_old4 = 0
    tw4 = Twist()

    rospy.init_node('botspeed', anonymous=True)
    
    rospy.Subscriber('bot1pose',Pose,bp1)
    b1pub = rospy.Publisher('bot1twist',Twist,queue_size = 10)

    rospy.Subscriber('bot2pose',Pose,bp2)
    b2pub = rospy.Publisher('bot2twist',Twist,queue_size = 10)

    rospy.Subscriber('bot3pose',Pose,bp3)
    b3pub = rospy.Publisher('bot3twist',Twist,queue_size = 10)

    rospy.Subscriber('bot4pose',Pose,bp4)
    b4pub = rospy.Publisher('bot4twist',Twist,queue_size = 10)

    while(True):
        x1 = bot1.position.x
        y1 = bot1.position.y
        z1 = bot1.orientation.z

        theta1 = 2 * (np.arctan(z1))

        vx1 = 20*(x1-xo1)
        vy1 = 20*(y1-yo1)
        wz1 = 20*(theta1 - theta_old1)

        tw1.linear.x = vx1
        tw1.linear.y = vy1
        tw1.angular.w = wz1
        b1pub.publish(tw1)
        xo1 = x1
        yo1 = y1 

        x2 = bot2.position.x
        y2 = bot2.position.y
        z2 = bot2.orientation.z

        theta2 = 2 * (np.arctan(z2))

        vx2 = 20*(x2-xo2)
        vy2 = 20*(y2-yo2)
        wz2 = 20*(theta2 - theta_old2)

        tw2.linear.x = vx2
        tw2.linear.y = vy2
        tw2.angular.w = wz2
        b2pub.publish(tw2)
        xo2 = x2
        yo2 = y2 

        x3 = bot3.position.x
        y3 = bot3.position.y
        z3 = bot3.orientation.z

        theta3 = 2 * (np.arctan(z3))

        vx3 = 20*(x3-xo3)
        vy3 = 20*(y3-yo3)
        wz3 = 20*(theta3 - theta_old3)

        tw3.linear.x = vx3
        tw3.linear.y = vy3
        tw3.angular.w = wz3
        b3pub.publish(tw3)
        xo3 = x3
        yo3 = y3

        x4 = bot4.position.x
        y4 = bot4.position.y
        z4 = bot4.orientation.z

        theta4 = 2 * (np.arctan(z4))

        vx4 = 20*(x4-xo4)
        vy4 = 20*(y4-yo4)
        wz4 = 20*(theta4 - theta_old4)

        tw4.linear.x = vx4
        tw4.linear.y = vy4
        tw4.angular.w = wz4
        b4pub.publish(tw4)
        xo4 = x4
        yo4 = y4 

        rate.sleep()

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass
