import numpy as np
import cv2
import os

# Load the calibration video
path = os.path.dirname(os.path.abspath(__file__))
grabber = cv2.VideoCapture(path+'/calibration.mp4')

# Load the calibration parameters
data = np.load(path+'/camera_parameters.npz')
mtx = data['name1']
dist = data['name2']

while (grabber.isOpened()):
    flag, img = grabber.read()
    if flag==False:
         break
    #利用求得的相机的内参和外参数据，可以对图像进行畸变的矫正
    undistortedImg = cv2.undistort(img, mtx, dist)

    cv2.imshow('img', img)
    cv2.waitKey(20)

cv2.destroyAllWindows()