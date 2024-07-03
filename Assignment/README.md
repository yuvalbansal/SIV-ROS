Assignment 1

Making a Catkin Workspace:
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin_make

Add source code “source ~/catkin_ws/devel/setup.bash” to ~/.bashrc
Creating package “image_processes”
cd src
catkin_create_pkg image_processes rospy
code .					(Open src folder in VSCode)

Add author information in “package.xml” 	(Optional)
cd .. 					(Go to catkin_ws)
catkin_make

Adding nodes in package:
cd catkin_ws/src/image_processes
mkdir scripts
cd scripts

Making Node 1 (Publish Web Cam image frames to topic Webcam_img)
touch webcam_publisher.py
chmod +x webcam_publisher.py			(To make the file executable)

Making Node 2 (Subscribe to topic Webcam_img and publish data to topic Webcam_cropped)
touch webcam_cropper.py
chmod +x webcam_cropper.py			(To make the file executable)

Making Node 3 (Subscribe to topic Webcam_cropped and show it)
touch webcam_viewer.py
chmod +x webcam_viewer.py			(To make the file executable)

To run all the nodes:
roslaunch image_processes image_cropping.launch
