import rospy
import cv2
import numpy as np
import rospy
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose

class bot_speed():
    def __init__(self):
        self.pos_old_x1 = 0 
        self.pos_old_y1 = 0
        self.twist_old_w1 = 0
        self.pos_old_x2 = 0 
        self.pos_old_y2 = 0
        self.twist_old_w2 = 0
        self.pos_old_x3 = 0 
        self.pos_old_y3 = 0
        self.twist_old_w3 = 0
        self.pos_old_x4 = 0 
        self.pos_old_y4 = 0
        self.twist_old_w4 = 0
        rospy.Subscriber("bot1pose",Pose,self.callback1)##I thought twist will be also in this message(ie)omega
        self.pub_s1 = rospy.Publisher("bot1twist",Twist, queue_size = 10)
        rospy.Subscriber("bot2pose",Pose,self.callback2)
        self.pub_s2 = rospy.Publisher("bot2twist",Twist, queue_size = 10)
        rospy.Subscriber("bot3pose",Pose,self.callback3)
        self.pub_s3 = rospy.Publisher("bot3twist",Twist, queue_size = 10)
        rospy.Subscriber("bot4pose",Pose,self.callback4)
        self.pub_s4 = rospy.Publisher("bot4twist",Twist, queue_size = 10)

    def callback1(self,msg):
        n = 1
        self.pos_x1  = msg.position.x
        self.pos_y1  = msg.position.y
        self.twist_w1 = msg.position.w
        self.dif_x1 = -(self.pos_old_x1 - self.pos_x1)
        self.dif_y1 = -(self.pos_old_y1 - self.pos_y1)
        self.dif_w1 = -(self.twist_old_w1 - self.twist_w1)
        self.pos_old_x1 = self.pos_x1
        self.pos_old_y1 = self.pos_y1
        self.twist_old_w1 = self.twist_w1
    
    def callback2(self,msg):
        n = 2
        self.pos_x2  = msg.position.x
        self.pos_y2  = msg.position.y
        self.twist_w2 = msg.position.w
        self.dif_x2 = -(self.pos_old_x2 - self.pos_x2)
        self.dif_y2 = -(self.pos_old_y2 - self.pos_y2)
        self.dif_w2 = -(self.twist_old_w2 - self.twist_w2)
        self.pos_old_x2 = self.pos_x2
        self.pos_old_y2 = self.pos_y2
        self.twist_old_w2 = self.twist_w2
    
    def callback3(self,msg):
        n = 3
        self.pos_x3  = msg.position.x
        self.pos_y3  = msg.position.y
        self.twist_w3 = msg.position.w
        self.dif_x3 = -(self.pos_old_x3 - self.pos_x3)
        self.dif_y3 = -(self.pos_old_y3 - self.pos_y3)
        self.dif_w3 = -(self.twist_old_w3 - self.twist_w3)
        self.pos_old_x3 = self.pos_x3
        self.pos_old_y3 = self.pos_y3
        self.twist_old_w3 = self.twist_w3

    def callback4(self,msg):
        n = 4
        self.pos_x4  = msg.position.x
        self.pos_y4  = msg.position.y
        self.twist_w4 = msg.position.w
        self.dif_x4 = -(self.pos_old_x4 - self.pos_x4)
        self.dif_y4 = -(self.pos_old_y4 - self.pos_y4)
        self.dif_w4 = -(self.twist_old_w4 - self.twist_w4)
        self.pos_old_x4 = self.pos_x4
        self.pos_old_y4 = self.pos_y4
        self.twist_old_w4 = self.twist_w4


if __name__ == '__main__':
    try:
        rospy.init_node('bottwistfind')
        rate = rospy.Rate(60)
        bs = bot_speed()
        tw = Twist()
        if n == 1:
            while(True):
                tw.linear.x1 = bs.dif_x1*60
                tw.linear.y1 = bs.dif_y1*60
                tw.angular.w1 = bs.dif_w1*60
        if n == 2:
            while True:    
                tw.linear.x2 = bs.dif_x2*60
                tw.linear.y2 = bs.dif_y2*60
                tw.angular.w2 = bs.dif_w2*60
        if n == 3:
            while True:
                tw.linear.x3 = bs.dif_x3*60
                tw.linear.y3 = bs.dif_y3*60
                tw.angular.w3 = bs.dif_w3*60
        if n == 4:
            while True:
                tw.linear.x4 = bs.dif_x4*60
                tw.linear.y4 = bs.dif_y4*60
                tw.angular.w4 = bs.dif_w4*60
            rate.sleep()

    except rospy.ROSInterruptException: pass
