## This is course material for Introduction to Modern Artificial Intelligence
## Class 9 Example code: depth_from_stereo.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

path = os.path.dirname(os.path.abspath(__file__))
imgL = cv.imread(path+'/tsukuba_l.png',0)
imgR = cv.imread(path+'/tsukuba_r.png',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()