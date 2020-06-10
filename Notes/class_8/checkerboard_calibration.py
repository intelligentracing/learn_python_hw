## This is course material for Introduction to Modern Artificial Intelligence
## Class 8 Example code: checkerboard_calibration.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import cv2
import os

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Define board size: (board_w x board_h)
board_w = 9
board_h = 6
blockSize = 25.8 / 1000 # in meter

# Prepare object points, like (0,0,0), (1,0,0), ...., (board_w-1,board_h-1,0)
objp = np.zeros((board_h*board_w,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)*blockSize

 # arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Load the calibration video
path = os.path.dirname(os.path.abspath(__file__))
grabber = cv2.VideoCapture(path+'/calibration.mov')
skipGrouping = 10
while (grabber.isOpened()):
    for i in range(skipGrouping):
        flag, img = grabber.read()
        if flag==False:
            break
    
    if flag==False:
        break

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
           
    # find the chess board (calibration pattern) corners
    flag, corners = cv2.findChessboardCorners(gray, (board_w ,board_h), None)

    # if calibration pattern is found, add object points,
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