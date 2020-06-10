import cv2
from cv2 import aruco
import numpy as np
import os


def main_write():
    NUM_MARKERS = 10

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    #drawMarker函数可以从由250个aruco标记组成的集合中选择给定id为i的标记，这250个标记的id由0~249表示。
    # drawMarker函数的第三个参数决定生成的标记的大小，它将生成200×200像素的图像。
    # 该函数还有第四第五个参数，第四个参数表示将要存储aruco标记的对象即输出的imgs。
    # 最后，第五个参数是边界宽度参数，它决定应将多少位（块）作为边界添加到生成的二进制图案中。

    #imgs表示将在200×200像素的图像中生成6x6位的图像。
    imgs = [aruco.drawMarker(aruco_dict, i, 200) for i in range(NUM_MARKERS)]
    for i in range(NUM_MARKERS):
        imname = "assets/" + str(i) + "_marker.jpg"
        cv2.imwrite(imname, imgs[i])
    print(len(imgs), "markers done!")


def main_detect():
    # Load a basic camera matrix and dist
    path = os.path.dirname(os.path.abspath(__file__))
    data = np.load(path + '/camera_parameters.npz')
    mtx = data['name1']
    dist = data['name2']
    print('Read intrinsic matrix:\n {}'.format(mtx))
    print('Read distortion array: {}'.format(dist))

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    #打开笔记本的摄像头cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret == False:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #初始化传递参数
        parameters = aruco.DetectorParameters_create()
        #检测marker需要阈值化
        parameters.adaptiveThreshConstant = 10
        #detectMarkers函数用于检测和确定标记角点的位置，gray是带有标记的场景图像。
        # aruco_dict是用于生成标记的字典。成功检测到的标记将存储在corners中，其ID存储在ids中。先前初始化的rParameters对象作为传递参数。
        corners, ids, rej = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
       #添加文字，正常尺寸的sans-serif字体
        font = cv2.FONT_HERSHEY_SIMPLEX
        if np.all(ids != None):
            #函数为了求R,T矩阵，第一个参数是角点坐标，第二个参数是marker大小
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, blockSize, mtx, dist)
            for i in range(0, ids.size):
                # draw axis for the aruco markers
                #frame是输入/输出图像，坐标将会在这张图像上绘制（通常就是检测marker的那张图像）。
                #rvec 和 tvec 是Pose参数，指明了坐标绘制的位置。
                #最后一个参数是坐标轴的长度，和tvec单位一样（通常是米）
                aruco.drawAxis(frame, mtx, dist, rvec[i], tvec[i], 0.02)

            # draw a square around the markers画外框
            aruco.drawDetectedMarkers(frame, corners)

            # code to show ids of the marker found
            strg = ''
            for i in range(0, ids.size):
                strg += str(ids[i][0]) + ', '

            cv2.putText(frame, "Id: " + strg, (0, 64), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(100)
        if key == ord('q'):
            break


if __name__ == '__main__':
    blockSize = 0.076  # block length unit is meter
    main_detect()  # 1950.2 is a dummmy value that works reasonably well on a MacBook Pro 2018
