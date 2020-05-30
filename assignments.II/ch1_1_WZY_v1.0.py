# Ex1 使用 Canny 算法中的 5x5 的 blur kernel，利用 cv2.filter2D, 模糊 
# 化处理我们提供的highway_video.mp4, 并将结果存在一个输出的AVI 文件中

import cv2
import numpy as np
import os

# load file
#文件位置
path = os.path.dirname(os.path.abspath(__file__))
#文件名称
filename = path + '/highway_video.mp4'
outputFilename = path + '/output_video.avi'
#抓取图像
grabber = cv2.VideoCapture(filename)
#图像基本信息(帧数,宽,高)
fps = int(grabber.get(cv2.CAP_PROP_FPS))
width = int(grabber.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(grabber.get(cv2.CAP_PROP_FRAME_HEIGHT))
#外放
output = cv2.VideoWriter(outputFilename, cv2.VideoWriter_fourcc('M', 'J', 'P','G'),\
     fps, (width, height), False)

#特定区域
def region_of_interest(image, height= None, width = None):
    if image is None:
        if (height is None) or (width is None):
            return None
    else:
        #裁剪
        height,width = image.shape
    #取值范围
    ROI = np.array([(0, height-100), (width, height-100), (width, height-300), (0, height-300)])
    #生成矩阵
    mask = np.zeros([height, width], dtype = np.uint8)
    #制作mask
    cv2.fillPoly(mask, [ROI], 255)
    return mask

#mask图片化
mask_image = region_of_interest(None, height, width)
#当抓取图像未结束时
while(grabber.isOpened()):
    #读取图像
    ret, frame = grabber.read()
    #如果放完了
    if ret == False:
        break

    # 创建灰度图像
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #edge_image = extract_edge(gray_image)
    edge_image = cv2.Canny(gray_image, 100, 200, L2gradient = True)
    
    kernel = np.ones((5,5), np.uint8)
    dilatedImage = cv2.dilate(edge_image, kernel, iterations = 3)

    ROI_image = cv2.bitwise_and(dilatedImage,mask_image)
    
    cv2.imshow('dilatedImage', ROI_image)
    output.write(ROI_image)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

#保存
grabber.release()
output.release()
cv2.destroyAllWindows()