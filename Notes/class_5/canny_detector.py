## This is course material for Introduction to Modern Artificial Intelligence
## Class 5 Example code: canny_detector.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import cv2
import numpy as np
import os

# 获取图像信息
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/highway_video.mp4'
outputFilename = path + '/output_video.avi'
#抓取每一帧
grabber = cv2.VideoCapture(filename)
#基本参数(约化为整)
fps = int(grabber.get(cv2.CAP_PROP_FPS))
width = int(grabber.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(grabber.get(cv2.CAP_PROP_FRAME_HEIGHT))
#输出cv2.VideoWriter(图片, cv2.VideoWriter_fourcc(文件格式),帧率, 图片大小, False)
output = cv2.VideoWriter(outputFilename, cv2.VideoWriter_fourcc('M', 'J', 'P','G'),\
     fps, (width, height), False)
#确认取值范围
def region_of_interest(image, height= None, width = None):
    #防止错误
    if image is None:
        if (height is None) or (width is None):
            return None
    else:
        height,width = image.shape
    #取值范围
    ROI = np.array([(0, height-100), (width, height-100), (width, height-300), (0, height-300)])
    #制作mask
    mask = np.zeros([height, width], dtype = np.uint8)
    #填充多边形fillPoly(图像, [顶点位置], 颜色)
    cv2.fillPoly(mask, [ROI], 255)
    #返回mask
    return mask

#生成mask
mask_image = region_of_interest(None, height, width)

while(grabber.isOpened()):
    #读取图像
    ret, frame = grabber.read()
    #若播放完成
    if ret == False:
        break
    #生成灰度图像
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #生成轮廓图像
    edge_image = cv2.Canny(gray_image, 100, 200, L2gradient = True)
    #图像合并
    ROI_image = cv2.bitwise_and(edge_image,mask_image)
    #展示图像
    cv2.imshow('Edge Image', ROI_image)
    #写入图像至视频
    output.write(ROI_image)
    #播放速度
    key = cv2.waitKey(1)
    #终止条件
    if key & 0xFF == ord('q'):
        break
#保存并删除窗口
grabber.release()
output.release()
cv2.destroyAllWindows()
