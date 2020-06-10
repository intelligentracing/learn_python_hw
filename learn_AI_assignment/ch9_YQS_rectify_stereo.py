import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# Load the stereo camera parameters
path = os.path.dirname(os.path.abspath(__file__))
data = np.load(path + '/stereo_parameters.npz')
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
min_disp = 16  # 最远的disparity
num_disp = 112 - min_disp
# 实现通过两个已经rectify的图像，逐行扫描，建立stereo matrix
stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                               numDisparities=num_disp,
                               blockSize=16,
                               P1=8 * 3 * window_size ** 2,
                               P2=32 * 3 * window_size ** 2,
                               disp12MaxDiff=1,
                               uniquenessRatio=10,
                               speckleWindowSize=100,
                               speckleRange=32)

# Compute the remap function to align the stereo images
rectify_scale = 1  # 0=full crop, 1=no crop
# stereoRectify() 的作用是为每个摄像头计算立体校正的映射矩阵。所以其运行结果并不是直接将图片进行立体矫正，而是得出进行立体矫正所需要的映射矩阵。
# R1-输出矩阵，第一个摄像机的校正变换矩阵（旋转变换）
# R2-输出矩阵，第二个摄像机的校正变换矩阵（旋转矩阵）
# P1-输出矩阵，第一个摄像机在新坐标系下的投影矩阵
# P2-输出矩阵，第二个摄像机在新坐标系下的投影矩阵
# Q-4*4的深度差异映射矩阵
# ROI1-可选的输出参数，Rect型数据。其内部的所有像素都有效
# ROI2-可选的输出参数，Rect型数据。其内部的所有像素都有效
R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(l_intrinsic, l_distortion, r_intrinsic, r_distortion, (640, 480), R,
                                                  T, alpha=rectify_scale)
# 计算畸变矫正和立体校正的映射变换，输出为映射变换,变换后的点坐标
left_maps = cv2.initUndistortRectifyMap(l_intrinsic, l_distortion, R1, P1, img_shape, cv2.CV_16SC2)
print(type(left_maps))
print(left_maps)
right_maps = cv2.initUndistortRectifyMap(r_intrinsic, r_distortion, R2, P2, img_shape, cv2.CV_16SC2)

for i in range(image_count):
    left_filename = path + '/left{:0>2d}'.format(i + 1) + '.jpg'
    right_filename = path + '/right{:0>2d}'.format(i + 1) + '.jpg'

    img_l = cv2.imread(left_filename, 0)
    img_r = cv2.imread(right_filename, 0)

    # Wrap left and right images to rectify能够得到输出图像中每一个点对应于输入图像中的该点的坐标
    # rmap重映射，就是把一幅图像中某位置的像素放置到另一个图片指定位置的过程,cv2.INTER_LANCZOS4为8×8像素邻域的Lanczos插值
    # img_l原图像，left_maps[0], left_maps[1]，分别表示原图像中各像素点的x,y坐标值
    left_img_remap = cv2.remap(img_l, left_maps[0], left_maps[1], cv2.INTER_LANCZOS4)
    right_img_remap = cv2.remap(img_r, right_maps[0], right_maps[1], cv2.INTER_LANCZOS4)

    # display_window is for visualizing the stereo pair after rectification
    # np.concatenate为了让两张图片并排显示
    display_window = np.concatenate((left_img_remap, right_img_remap), axis=1)
    display_window = cv2.cvtColor(display_window, cv2.COLOR_GRAY2BGR)

    # Draw lines parallel to baseline
    for j in range(0, img_shape[1], 20):
        cv2.line(display_window, (0, j), (img_shape[0] + img_shape[0], j), (0, 255, 0), 1, 8)

    cv2.imshow('stereo rectify', display_window)
    key = cv2.waitKey()
    if key == ord('q'):
        break

    # Compute the display the disparity由此测得空间的深度，不同的颜色深度代表不同的disparity即代表不同的深度
    disparity = stereo.compute(left_img_remap, right_img_remap)
    plt.imshow(disparity, 'gray')
    plt.show()
