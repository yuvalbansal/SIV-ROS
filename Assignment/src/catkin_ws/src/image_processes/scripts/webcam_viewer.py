#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    # Convert the ROS image message to an OpenCV image
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    
    # Display the image
    cv2.imshow("Webcam Cropped Image", cv_image)
    cv2.waitKey(1)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('webcam_viewer', anonymous=True)
    
    # Create a subscriber for the "Webcam_cropped" topic
    rospy.Subscriber('Webcam_cropped', Image, image_callback)
    
    # Initialize the OpenCV window
    cv2.namedWindow("Webcam Cropped Image", cv2.WINDOW_NORMAL)
    
    rospy.spin()
    
    # Close the OpenCV window when the node is shut down
    cv2.destroyAllWindows()
