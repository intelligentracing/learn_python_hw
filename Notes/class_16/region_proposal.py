## This is course material for Introduction to Modern Artificial Intelligence
## Class 16 Example code: region_proposal.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import cv2
import os

DEBUG = True

# load the test image: three_horses.jpg
path = os.path.dirname(os.path.abspath(__file__))
image = cv2.imread(path+'/zebras.jpg')
object_string = 'zebra'

def selective_search(image, method = 'fast'):
    # Call opencv selective search module
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(image)

    # Choose between fast and standard implementation
    if method == "fast":
        ss.switchToSelectiveSearchFast()
    elif method == "quality":
        ss.switchToSelectiveSearchQuality()
    else:
        print("Unknown method value.")
        raise ValueError

	# run selective search on the input image
    rects = ss.process()
	# return the region proposal bounding boxes
    return rects

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
    #numpy与opencv坐标表示顺序不同
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

            if DEBUG:
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                detect_display = cv2.rectangle(detect_display, top_left, bottom_right, (0,0, 255), 2)

if DEBUG:
    cv2.imshow('ResNet50 Detection', detect_display)
    cv2.waitKey(0)

# Non-Maximum Suppression next