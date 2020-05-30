## This is course material for Introduction to Modern Artificial Intelligence
## Class 5 Example code: adaptive_thresholding.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use
#thresholding 阈值
import cv2
import numpy as np
import os
#文件路径
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/bookpage.jpg'
#数据读取
image = cv2.imread(filename)
#展示图像(标题,图像)
cv2.imshow('Original', image)
#生成灰度图像
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Process 1: 使用静态阈值算法
#返回值有两个,第一个不要
#cv2.threshold(图象名称, , 白, 算法(此处设置的是二元(非黑即白)))
_, threshImage = cv2.threshold(grayImage, 20, 255, cv2.THRESH_BINARY)
#展示图像(标题,图像)
cv2.imshow('Threshold', threshImage)

# Process 2: 使用动态阈值算法
#返回值有两个,第一个不要
#cv2.adaptiveThreshold(图象名称, 白, 降噪,算法(此处设置的是二元(非黑即白)),样本区域,1)
adaptiveImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#展示图像(标题,图像)
cv2.imshow('Adaptive',adaptiveImage)
#等待时间(单位毫秒)
cv2.waitKey(0)