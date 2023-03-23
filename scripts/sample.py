#!/usr/bin/env python3

from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError
import rospy
import cv2
import sys

class ChaseJuellyBonny:
    def __init__(self):
        rospy.init_node("ChaseJuellyBonny")
        self.bridge = CvBridge()
        self.twist = Twist()

        self.frame = None
        self.break_frag = False

        self.pub = rospy.Publisher('tello/cmd_vel', Twist, queue_size=10)
        rospy.loginfo('read')
        self.sub = rospy.Subscriber('tello/image_raw', Image, self.get_img)
        self.main()

    def get_img(self, data):
        try:
            self.frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError:
            rospy.logerr('Camera Err')
            sys.exit()
        '''
        cv2.imshow('camera0', self.frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            self.break_frag = True
        '''
    def main(self):
        while not rospy.is_shutdown():
            if self.frame is None:
                rospy.loginfo('wait for get camera')
                continue
            cv2.imshow('camera1', self.frame)
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break


if __name__ == '__main__':
    try:
        test = ChaseJuellyBonny()
    except rospy.ROSInterruptException:pass
