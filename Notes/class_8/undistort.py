## This is course material for Introduction to Modern Artificial Intelligence
## Class 8 Example code: undistort.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import cv2
import os

# 加载视频
path = os.path.dirname(os.path.abspath(__file__))
grabber = cv2.VideoCapture(path+'/calibration.mov')

#加载滤镜
data = np.load(path+'/camera_parameters.npz')
mtx = data['name1']
dist = data['name2']

while (grabber.isOpened()):
    flag, img = grabber.read()
    if flag==False:
         break
    #修正图片
    undistortedImg = cv2.undistort(img, mtx, dist)

    cv2.imshow('img', img)
    cv2.waitKey(20)

cv2.destroyAllWindows()