#!/usr/bin/env python3

### lib
import rospy
import math
import tf
import time

### msg lib
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class Takeoff():
    def __init__(self):
        self.empty = Empty()
        self.takeoff = rospy.Publisher('/tello/takeoff', Empty, queue_size=10)
        while self.takeoff.get_num_connections() < 1:
            continue

    def execute(self):
        self.takeoff.publish(self.empty)
        rospy.loginfo('takeoff')
        time.sleep(7)

class Land():
    def __init__(self):
        self.empty = Empty()
        self.land = rospy.Publisher('/tello/land', Empty, queue_size=10)
        while self.land.get_num_connections() < 1:
            continue

    def execute(self):
        self.land.publish(self.empty)
        rospy.loginfo('landing')

rospy.init_node('test')
t = Takeoff()
t.execute()
l = Land()
l.execute()
