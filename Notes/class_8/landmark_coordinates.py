## This is course material for Introduction to Modern Artificial Intelligence
## Class 8 Example code: landmark_coordinates.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please use conda to install aruco as: conda install -c conda-forge aruco
import cv2
from cv2 import aruco
import numpy as np
import os

def main_write():
    NUM_MARKERS = 10

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    imgs = [aruco.drawMarker(aruco_dict,i,200) for i in range(NUM_MARKERS)]
    for i in range(NUM_MARKERS):
        imname = "assets/" + str(i) + "_marker.jpg"
        cv2.imwrite(imname, imgs[i])
    print (len(imgs), "markers done!")

def main_detect():
    # Load a basic camera matrix and dist
    path = os.path.dirname(os.path.abspath(__file__))
    data = np.load(path+'/camera_parameters.npz')
    mtx = data['name1']
    dist = data['name2']
    print('Read intrinsic matrix:\n {}'.format(mtx))
    print('Read distortion array: {}'.format(dist))
    
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret==False:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        parameters = aruco.DetectorParameters_create()
        parameters.adaptiveThreshConstant = 10
        corners, ids, rej = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        font = cv2.FONT_HERSHEY_SIMPLEX
        if np.all(ids!= None):
            rvec, tvec ,_ = aruco.estimatePoseSingleMarkers(corners, blockSize, mtx, dist)

            for i in range(0, ids.size):
                # draw axis for the aruco markers
                aruco.drawAxis(frame, mtx, dist, rvec[i], tvec[i], 0.02)

            # draw a square around the markers
            aruco.drawDetectedMarkers(frame, corners)

            # code to show ids of the marker found
            strg = ''
            for i in range(0, ids.size):
                strg += str(ids[i][0])+', '

            cv2.putText(frame, "Id: " + strg, (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(100)
        if key == ord('q'):
            break

if __name__ == '__main__':
    blockSize = 0.076 # block length unit is meter
    main_detect() #1950.2 is a dummmy value that works reasonably well on a MacBook Pro 2018


