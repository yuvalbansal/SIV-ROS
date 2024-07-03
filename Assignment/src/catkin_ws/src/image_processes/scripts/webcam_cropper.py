#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    # Convert the ROS image message to an OpenCV image
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    
    # Crop the image by 30%
    height, width, _ = cv_image.shape
    crop_width = int(width * 0.3)
    crop_height = int(height * 0.3)
    cropped_image = cv_image[crop_height:-crop_height, crop_width:-crop_width]
    
    # Publish the cropped image
    cropped_pub.publish(bridge.cv2_to_imgmsg(cropped_image, encoding="bgr8"))

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('webcam_cropper', anonymous=True)
    
    # Create a subscriber for the "Webcam_img" topic
    rospy.Subscriber('Webcam_img', Image, image_callback)
    
    # Create a publisher for the "Webcam_cropped" topic
    cropped_pub = rospy.Publisher('Webcam_cropped', Image, queue_size=10)
    
    rospy.spin()
