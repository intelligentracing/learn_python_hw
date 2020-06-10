import numpy as np
import cv2
import os
#criteria是设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Define board size: (board_w x board_h)
board_w = 9
board_h = 6
blockSize = 26.2 / 1000  # in meter 26.2是毫米为单位的

# Prepare object points, like (0,0,0), (1,0,0), ...., (board_w-1,board_h-1,0)
objp = np.zeros((board_h * board_w, 3), np.float32)
# 获得check board角点坐标在世界坐标系下的真实坐标值objp本身是三列，但是np.mgrid生成的是两列，所以objp只能取2列
objp[:, :2] = np.mgrid[0:board_w, 0:board_h].T.reshape(-1, 2) * blockSize

# arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

# Load the calibration video
path = os.path.dirname(os.path.abspath(__file__))
grabber = cv2.VideoCapture(path + '/calibration.mp4')
skipGrouping = 10  # 每10帧记录一帧，节省计算资源
image_count = 0
while (grabber.isOpened()):
    for i in range(skipGrouping):
        flag, img = grabber.read()

        if flag == False:
            break

    if flag == False:
            break
    image_count = image_count + 1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # find the chess board (calibration pattern) corners
    # 函数作用为提取角点，(board_w ,board_h)为check board上内角点的行列数，一般不相同，
    # 便于后续标定程序识别标定板的方向，如果找到 flag= true
    #corner用于存储检测到的内角点图像坐标位置，一般是数组形式
    flag, corners = cv2.findChessboardCorners(gray, (board_w, board_h), None)

    # if calibration pattern is found, add object points,
    # image points (after refining them)
    if flag == True:
        objpoints.append(objp)#将空间中角点坐标加入到之前的列表中

        # Refine the corners of the detected corners
        # 为了提高标定精度，降低相机标定偏差，(11, 11)是搜索窗口的大小，winsize为搜索窗口的一半这里是（5，5）
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners函数用于绘制被成功标定的角点
        #(board_w, board_h)每张标定棋盘上内角点的行列数，
        # corners2初始的角点坐标向量，同时作为亚像素坐标位置的输出，所以需要是浮点型数据
        #标志位，用来指示定义的棋盘内角点是否被完整的探测到，
        # true表示别完整的探测到，函数会用直线依次连接所有的内角点，作为一个整体，
        # false表示有未被探测到的内角点，这时候函数会以（红色）圆圈标记出检测到的内角点；
        img = cv2.drawChessboardCorners(img, (board_w, board_h), corners2, flag)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# Call calibration function
print('Calculating the camera parameters from {} images ...'.format(image_count))
#函数用于标定相机内外参数
#gray.shape[::-1]是图像的尺寸大小
# mtx内变换矩阵的参数，dist是畸变系数，rvecs和tvecs是每张图片的外变换矩阵，即平移向量和旋转向量
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Save the camera parameters into a numpy binary file
# savez在一个numpy文件中存储多了变量
np.savez(path + '\camera_parameters', name1=mtx, name2=dist)
print('Saved intrinsic matrix: \n {}'.format(mtx))
print('Saved distortion array: {}'.format(dist))