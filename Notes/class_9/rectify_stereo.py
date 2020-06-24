## This is course material for Introduction to Modern Artificial Intelligence
## Class 9 Example code: rectify_stereo.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

#打开文件,初始化存储数据
path = os.path.dirname(os.path.abspath(__file__))
data = np.load(path+'/stereo_parameters.npz')
#修正前后数据
l_intrinsic = data['name1']
l_distortion = data['name2']
r_intrinsic = data['name3']
r_distortion = data['name4']
R = data['name5']
T = data['name6']
img_shape = tuple(data['name7'])
image_count = 14

# Initialize StereoSGBM stereo matching method
window_size = 3
min_disp = 16
num_disp = 112-min_disp
stereo = cv2.StereoSGBM_create(minDisparity = min_disp,
        numDisparities = num_disp,
        blockSize = 16,
        P1 = 8*3*window_size**2,
        P2 = 32*3*window_size**2,
        disp12MaxDiff = 1,
        uniquenessRatio = 10,
        speckleWindowSize = 100,
        speckleRange = 32)

# Compute the remap function to align the stereo images
rectify_scale = 1 # 0=full crop, 1=no crop
R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(l_intrinsic, l_distortion, r_intrinsic, r_distortion, (640, 480), R, T, alpha = rectify_scale)
left_maps = cv2.initUndistortRectifyMap(l_intrinsic, l_distortion, R1, P1, img_shape, cv2.CV_16SC2)
right_maps = cv2.initUndistortRectifyMap(r_intrinsic, r_distortion, R2, P2, img_shape, cv2.CV_16SC2)

for i in range(image_count):
    left_filename = path + '/left{:0>2d}'.format(i+1) + '.jpg'
    right_filename = path + '/right{:0>2d}'.format(i+1) + '.jpg'

    img_l = cv2.imread(left_filename, 0)
    img_r = cv2.imread(right_filename, 0)

    # Wrap left and right images to rectify
    left_img_remap = cv2.remap(img_l, left_maps[0], left_maps[1], cv2.INTER_LANCZOS4)
    right_img_remap = cv2.remap(img_r, right_maps[0], right_maps[1], cv2.INTER_LANCZOS4)

    # display_window is for visualizing the stereo pair after rectification
    display_window = np.concatenate((left_img_remap, right_img_remap), axis = 1)
    display_window = cv2.cvtColor(display_window, cv2.COLOR_GRAY2BGR)
    
    # Draw lines parallel to baseline
    for j in range(0, img_shape[1], 20):
        cv2.line(display_window, (0, j), (img_shape[0]+img_shape[0], j), (0, 255, 0), 1, 8)

    cv2.imshow('stereo rectify', display_window)
    key = cv2.waitKey()
    if key == ord('q'):
        break
    
    # Compute the display the disparity
    disparity= stereo.compute(left_img_remap, right_img_remap)
    plt.imshow(disparity,'gray')
    plt.show()
