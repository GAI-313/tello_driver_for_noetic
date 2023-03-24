#!/usr/bin/env python3

# import the lib of message type
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from sensor_msgs.msg import Image

# import the lins for get video
from cv_bridge import CvBridge, CvBridgeError # use image massage in ROS
import rospy
import cv2 # OpenCV
import sys

# make a class
class ChaseJuellyBonny:
    # initialize function (method)
    def __init__(self):
        rospy.init_node("ChaseJuellyBonny") # node name
        self.bridge = CvBridge()
        self.twist = Twist()

        self.frame = None
        self.break_frag = False

        self.pub = rospy.Publisher('tello/cmd_vel', Twist, queue_size=10)
        rospy.loginfo('read')
        self.sub = rospy.Subscriber('tello/image_raw', Image, self.get_img) # get image message from this topic
        self.main()

    def get_img(self, data):
        try:
            self.frame = self.bridge.imgmsg_to_cv2(data, "bgr8") # encode rgb data from Image message
        except CvBridgeError: # if error about image is occured. stop the node.
            rospy.logerr('Camera Err')
            sys.exit()

    def main(self):
        while not rospy.is_shutdown(): # roop
            if self.frame is None: # if not come the image data. wait
                rospy.loginfo('wait for get camera')
                continue
            cv2.imshow('camera1', self.frame) # show
            key = cv2.waitKey(1) & 0xFF # keyboad detection
            if key == 27:
                break


if __name__ == '__main__':
    try:
        test = ChaseJuellyBonny() # define variable from class
    except rospy.ROSInterruptException:pass
