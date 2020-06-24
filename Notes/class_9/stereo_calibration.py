## This is course material for Introduction to Modern Artificial Intelligence
## Class 9 Example code: stereo_calibration.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use
import numpy as np
import cv2
import os
import sys

criteria = (cv2.TERM_CRITERIA_COUNT + cv2.TERM_CRITERIA_EPS, 200, sys.float_info.epsilon)

# Define board size: (board_w x board_h)
board_w = 9
board_h = 6
blockSize = 1 # for Unknown physical length, set it up to scale as unit length
image_count = 14

# Prepare object points, like (0,0,0), (1,0,0), ...., (board_w-1,board_h-1,0)
objp = np.zeros((board_h*board_w,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)*blockSize

 # arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
l_imgpoints = [] # 2d points in left image plane.
r_imgpoints = [] # 2d points in right image plane.

# Load the calibration video
path = os.path.dirname(os.path.abspath(__file__))

# Calibrate left and right cameras separately first
for i in range(image_count):
    left_filename = path + '/left{:0>2d}'.format(i+1) + '.jpg'
    right_filename = path + '/right{:0>2d}'.format(i+1) + '.jpg'

    img_l = cv2.imread(left_filename, 0)
    img_r = cv2.imread(right_filename, 0)
        
    if (img_l is None) or (img_r is None):
        continue

    # find the chess board (calibration pattern) corners
    flag_l, corners_l = cv2.findChessboardCorners(img_l, (board_w ,board_h), None)
    flag_r, corners_r = cv2.findChessboardCorners(img_r, (board_w ,board_h), None)

    # if both left and right calibration patterns are found, add object points,
    # image points (after refining them)
    if flag_l == True and flag_r == True:
        objpoints.append(objp)

        # Refine the corners of the detected corners
        corners2 = cv2.cornerSubPix(img_l, corners_l,(11,11),(-1,-1),criteria)
        l_imgpoints.append(corners2)
        corners2 = cv2.cornerSubPix(img_r, corners_r,(11,11),(-1,-1),criteria)
        r_imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img_r, (board_w ,board_h), corners2, True)
        cv2.imshow('img', img)
        cv2.waitKey(500)

print('Calibrate stereo cameras from {} images ...'.format(len(objpoints)))
ret, l_intrinsic, l_distortion, rvecs, tvecs = cv2.calibrateCamera(objpoints, l_imgpoints, img.shape[::-1],None,None)
ret, r_intrinsic, r_distortion, rvecs, tvecs = cv2.calibrateCamera(objpoints, r_imgpoints, img.shape[::-1],None,None)

# Calibrate the stereo camera
ret, l_intrinsic, l_distortion, r_intrinsic, r_distortion, R, T, _, _ = cv2.stereoCalibrate(objpoints, \
    l_imgpoints, r_imgpoints, l_intrinsic, l_distortion, r_intrinsic, r_distortion, img.shape[::-1], \
        R=None, T=None, E=None, F=None, criteria = criteria)

print('Rotation = \n {}'.format(R))
print('Translation = \n {}'.format(T))

# Save the calibration parameters
np.savez(path+'\stereo_parameters', name1 = l_intrinsic, name2 = l_distortion, name3 = r_intrinsic, name4=r_distortion,\
    name5 = R, name6 = T, name7 = img.shape[::-1])