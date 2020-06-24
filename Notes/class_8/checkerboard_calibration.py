## This is course material for Introduction to Modern Artificial Intelligence
## Class 8 Example code: checkerboard_calibration.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import cv2
import os

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

#确认棋盘大小
board_w = 9
board_h = 6
#确定格子大小
blockSize = 25.8 / 1000

# 准备空数组并将深度设为0
objp = np.zeros((board_h*board_w,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)*blockSize

#初始化存储数据的数组
objpoints = []
imgpoints = [] 
#加载录像
path = os.path.dirname(os.path.abspath(__file__))
grabber = cv2.VideoCapture(path+'/calibration.mov')
#取帧
skipGrouping = 1
#读取每一帧的数据
while (grabber.isOpened()):
    for i in range(skipGrouping):
        flag, img = grabber.read()
        if flag==False:
            break
    
    if flag==False:
        break
#灰度化图像
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
           
    #找到棋盘各角
    flag, corners = cv2.findChessboardCorners(gray, (board_w ,board_h), None)

    # 当可以识别时
    # image points (after refining them)
    if flag == True:
        objpoints.append(objp)

        # Refine the corners of the detected corners
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (board_w ,board_h), corners2, flag)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

if len(objpoints)>0:
    # Call calibration function
    print('Calculating the camera parameters from {} images ...'.format(len(objpoints)))
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

    # Save the camera parameters into a numpy binary file
    np.savez(path+'/camera_parameters', name1=mtx, name2=dist)
    print('Saved intrinsic matrix: \n {}'.format(mtx))
    print('Saved distortion array: {}'.format(dist))