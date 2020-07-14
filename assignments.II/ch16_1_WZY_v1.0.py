## This is course material for Introduction to Modern Artificial Intelligence
## Class 16 Example code: sliding_window.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
import cv2
import os

DEBUG = True

#加载模型
model = ResNet50(weights='imagenet')
#设置基础参数
window_size = 128
#单个窗口大小
sliding_window_step = 8
#检测步长
detection_threshold = 0.8
#可信数据阈值
downsample_ratio = 2
#缩小比例

# load the test image: three_horses.jpg
path = os.path.dirname(os.path.abspath(__file__))
image = cv2.imread(path+'/zebras.jpg')

def sliding_window_detector(image, window_size, step, classifier, object_string, debug = False):
    ''' The function deploys a generic classifier to detect ROI in images using step size 
    sliding windows. 
    Input: Expect classifier input to be window_size*window_size, pattern is defined in object_string
    Output: classification probability [0, 1] at each sliding window point
    '''
    image_H, image_W, image_D = image.shape
    return_probability = np.zeros((image_H,image_W))

    if debug:
        debug_image = image.copy()

    print('Detecting {0}x{1}'.format(image_H, image_W))
    #遍历图片
    for h in range(0, image_H-window_size, step):
        for w in range(0, image_W - window_size, step):
            image_window = image[h:h+window_size, w:w+window_size,:]
            image_window = image_window.reshape((1, window_size, window_size, 3))

            # Sent sliding window into ResNet DNN classifier
            image_window = preprocess_input(image_window)
            y_predict = model.predict(image_window)
            label = decode_predictions(y_predict)

            # Look for the pattern defined in object_string and probability > detection_threshold
            for label_index in range(5):
                if label[0][label_index][1] == object_string and \
                    label[0][label_index][2]>detection_threshold:
                    return_probability[h, w] = label[0][label_index][2]
                    print('*', end='')

                    if debug: 
                        # Draw a bounding box at detected region
                        top_left_corner = (w, h)
                        bottom_right_corner = (w+window_size, h+window_size)
                        debug_image = cv2.rectangle(debug_image, top_left_corner, bottom_right_corner, (0,0,255), 4) 
                        cv2.imshow('Sliding Window', debug_image)
                        cv2.waitKey(10)
    print('Done!')
    return return_probability

downsample_stages = 3
multi_scale_detection = []   # Used to store multi-scale probability returns

# First firther reduce the image size one time to reduce processing time
image_H, image_W, image_D = image.shape
image = cv2.resize(image, (int(image_W/downsample_ratio ), int(image_H/downsample_ratio)))
for downsample in range(downsample_stages):
    image_H, image_W, image_D = image.shape
    image_H = int(image_H/downsample_ratio); image_W = int(image_W/downsample_ratio)
    image = cv2.resize(image, (image_W, image_H))
    multi_scale_detection.append(sliding_window_detector(image, window_size, sliding_window_step, 
        model, 'zebra', DEBUG))

    if DEBUG:
        print('One scale is complete. Press any key to continue or save debug image ...')
        cv2.waitKey(0)

# def nfs ():
