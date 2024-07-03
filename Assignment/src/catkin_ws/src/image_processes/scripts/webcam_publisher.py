#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def webcam_publisher():
    # Initialize the ROS node
    rospy.init_node('webcam_publisher', anonymous=True)
    
    # Create a publisher for the "Webcam_img" topic
    image_pub = rospy.Publisher('Webcam_img', Image, queue_size=10)
    
    # Initialize the OpenCV video capture
    cap = cv2.VideoCapture(0)  # Use index 0 for the default webcam
    
    # Initialize the CvBridge object
    bridge = CvBridge()
    
    rate = rospy.Rate(10)  # Publish at a rate of 10 Hz
    
    while not rospy.is_shutdown():
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if ret:
            # Convert the frame to a ROS image message
            img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            
            # Publish the image message
            image_pub.publish(img_msg)
        
        rate.sleep()

    # Release the webcam and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        webcam_publisher()
    except rospy.ROSInterruptException:
        pass
