#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Bool
#from pishu_msgs.srv import talk
import os
from functools import partial

def chatter_callback(done_pub, data):
    print data.data
    cmd = "espeak ' " + data.data + " '  2>/dev/null "
    print cmd
    os.system(cmd)
    #global done_pub
    done_pub.publish(True)


def listener():

    rospy.init_node('mouth', anonymous=False)

    done_pub = rospy.Publisher("mouth/done", Bool, queue_size = 5)

    rospy.Subscriber("mouth/chatter", String, partial(chatter_callback, done_pub))

    rospy.spin()

if __name__ == '__main__':
    listener()    
