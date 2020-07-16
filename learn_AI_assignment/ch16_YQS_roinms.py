## This is course material for Introduction to Modern Artificial Intelligence
## Class 16 Example code: region_proposal.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import cv2
import os
import numpy as np

DEBUG = True

# load the test image: three_horses.jpg
path = os.path.dirname(os.path.abspath(__file__))
image = cv2.imread(path+'/zebras.jpg')
object_string = 'zebra'

def selective_search(image, method = 'fast'):
    # Call opencv selective search module，建立selective search分割器
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

    ss.setBaseImage(image)

    # Choose between fast and standard implementation
    if method == "fast":#快速模式精确度较差
        ss.switchToSelectiveSearchFast()
    elif method == "quality":#精确模式
        ss.switchToSelectiveSearchQuality()
    else:
        print("Unknown method value.")
        raise ValueError

	# run selective search on the input image
    rects = ss.process()
	# return the region proposal bounding boxes
    return rects

def nms(x1, y1, x2, y2, scores, thresh):
    # initialize the list of picked indexes
    # x1、y1、x2、y2、以及score赋值
    x1 = np.array(x1)
    y1 = np.array(y1)
    x2_h = np.array(x2)
    x2 = x1 + x2_h
    y2_w = np.array(y2)
    y2 = y1 + y2_w
    scores = np.array(scores)
    # 每一个候选框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = scores.argsort()  # 应该反过来
    # order是按照score降序排序的
    # order = scores.argsort()[::-1]

    pick = []
    while len(idxs) > 0:
        # grab the last index in the indexes list, add the index
        # value to the list of picked indexes, then initialize
        # the suppression list (i.e. indexes that will be deleted)
        # using the last index
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        suppress = [last]
        for pos in range(0, last):
            # grab the current index
            j = idxs[pos]
            # find the largest (x, y) coordinates for the start of
            # the bounding box and the smallest (x, y) coordinates
            # for the end of the bounding box
            xx1 = max(x1[i], x1[j])
            yy1 = max(y1[i], y1[j])
            xx2 = min(x2[i], x2[j])
            yy2 = min(y2[i], y2[j])
            # compute the width and height of the bounding box
            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)
            # compute the ratio of overlap between the computed
            # bounding box and the bounding box in the area list
            overlap = float(w * h) / areas[j]
            # if there is sufficient overlap, suppress the
            # current bounding box
            if overlap > thresh:
                suppress.append(pos)
        # delete all indexes from the index list that are in the
        # suppression list
        idxs = np.delete(idxs, suppress)
    # return only the bounding boxes that were picked
    return x1[pick], y1[pick],x2[pick], y2[pick]


# First reduce the image size to reasonable for speed
image_H, image_W, image_D = image.shape
image = cv2.resize(image, (int(image_W/3 ), int(image_H/3)))

print('Detecting {0}x{1}'.format(int(image_W/3 ), int(image_H/3)))
selected_rects = selective_search(image, 'quality')

# Load a generic image classifier
model = ResNet50(weights='imagenet')
# Set demo parameters
window_size = 224
detection_threshold = 0.9
max_classify_number = 200

if DEBUG:
    # display selected rects
    search_display = image.copy()
    detect_display = image.copy()
    for (x, y, w, h) in selected_rects[0:min(max_classify_number, len(selected_rects))]:
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        display = cv2.rectangle(search_display, top_left, bottom_right, (0,0, 255), 2)
    cv2.imshow('Selective Search', search_display)
    cv2.waitKey(0)

# Classify rects
image_H, image_W, image_D = image.shape
detect_probability = [[[] for w in range(image_W)] for h in range(image_H)]
for (x, y, w, h) in selected_rects[0:min(max_classify_number, len(selected_rects))]:
    # Call ResNet50
    ROI = image[y:y+h, x:x+w, :]
    ROI = cv2.resize(ROI, (224,224))
    ROI = ROI.reshape((1, window_size, window_size, 3))
    ROI = preprocess_input(ROI)
    y_predict = model.predict(ROI)
    label = decode_predictions(y_predict)

    for label_index in range(5):
        if label[0][label_index][1] == object_string and \
             label[0][label_index][2]>detection_threshold:
            detect_probability[y][x] = [label[0][label_index][2], (x, y, w, h)]

            # if DEBUG:
            #     top_left = (x, y)
            #     bottom_right = (x + w, y + h)
            #     detect_display = cv2.rectangle(detect_display, top_left, bottom_right, (0,0, 255), 2)
if DEBUG:
    debug_image = image.copy()
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    score = []
    for i in range(image_H):
        for j in range(image_W):
            if detect_probability[i][j] != []:
                x1.append(detect_probability[i][j][1][1])
                y1.append(detect_probability[i][j][1][0])
                x2.append(detect_probability[i][j][1][3])
                y2.append(detect_probability[i][j][1][2])
                score.append(detect_probability[i][j][0])

    x_box, y_box, x2_box, y2_box = nms(x1, x2, x2, y2, score, 0.5)  # 0.3为faster-rcnn中配置文件的默认值
    for x1, y1, x2, y2 in zip(x_box, y_box,x2_box, y2_box):
        top_left_corner = (x1, y1)
        bottom_right_corner = (x2, y2)
        debug_image = cv2.rectangle(debug_image, top_left_corner, bottom_right_corner, (0, 0, 255), 4)
    cv2.imshow('ResNet50 Detection', debug_image)
    cv2.waitKey(0)



# if DEBUG:
#     cv2.imshow('ResNet50 Detection', detect_display)
#     cv2.waitKey(0)

# Non-Maximum Suppression next
