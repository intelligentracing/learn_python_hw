# Ex2 修改 floodfill 代码的 29 行，添加有关 mask 的一个用途。请参 照关于 floorfill 中的 mask 使用说明

## This is course material for Introduction to Modern Artificial Intelligence
## Class 5 Example code: floodfill_segmentation.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import cv2
import numpy as np
import os


# load file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/highway_video.mp4'
outputFilename = path + '/rgb_floodfill.avi'
grabber = cv2.VideoCapture(filename)
fps = int(grabber.get(cv2.CAP_PROP_FPS))
width = int(grabber.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(grabber.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter(outputFilename, cv2.VideoWriter_fourcc('M', 'J', 'P','G'),\
     fps, (width, height), True)
def region_of_interest(image, height= None, width = None):
    if image is None:
        if (height is None) or (width is None):
            return None
    else:
        #裁剪
        height,width = image.shape
    #生成矩阵
    mask = np.ones([height+2, width+2], dtype = np.uint8)
    mask[height-300 : height - 60, 0 : width] = 0
    #制作mask
    return mask
# mask –
# Operation mask that should be a single-channel 8-bit image, 2 pixels wider and 2 pixels taller than image. 
# Since this is both an input and output parameter, you must take responsibility of initializing it. 
# Flood-filling cannot go across non-zero pixels in the input mask. For example, an edge detector output 
# can be used as a mask to stop filling at edges. On output, pixels in the mask corresponding to filled 
# pixels in the image are set to 1 or to the a value specified in flags as described below. It is therefore 
# possible to use the same mask in multiple calls to the function to make sure the filled areas do not overlap.

while(grabber.isOpened()):
    ret, frame = grabber.read()
    mask_image = region_of_interest(None, height, width)
    seed = (width//2, height-150)
    # Flood the frame to segment only the road
    cv2.floodFill(frame,seedPoint = seed,newVal = (255, 0, 0), loDiff=(3,3,3), upDiff = (3,3,3),mask=mask_image)
    # Augment the illustration of the seed point
    cv2.circle(frame, seed, 2, (0, 0, 255), cv2.FILLED, cv2.LINE_AA)
    output.write(frame)
    cv2.imshow('Road', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
grabber.release()
output.release()
cv2.destroyAllWindows()