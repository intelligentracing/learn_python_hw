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

try:
    while(grabber.isOpened()):
        ret, frame = grabber.read()
        if ret == False:
            break

        seed = (width//2, height-100)
       

        # cv2.floodFill(img,mask,seed,newvalue(BGR),(loDiff1,loDiff2,loDiff3),(upDiff1,upDiff2,upDiff3),flag)
        # img：为待使用泛洪算法的图像
        # mask：为掩码层，使用掩码可以规定是在哪个区域使用该算法，如果是对于完整图像都要使用，则掩码层大小为原图行数+2，列数+2.
        #       是一个二维的0矩阵，边缘一圈会在使用算法是置为1。而只有对于掩码层上对应为0的位置才能泛洪，所以掩码层初始化为0矩阵。【dtype:np.uint8】
        # seed：为泛洪算法的种子点，也是根据该点的像素判断决定和其相近颜色的像素点，是否被泛洪处理。
        # newvalue：是对于泛洪区域新赋的值（B,G,R）
        # (loDiff1,loDiff2,loDiff3)：是相对于seed种子点像素可以往下的像素值，即seed(B0,G0,R0)，泛洪区域下界为（B0-loDiff1,G0-loDiff2,R0-loDiff3）
        # (upDiff1,upDiff2,upDiff3)：是相对于seed种子点像素可以往上的像素值，即seed(B0,G0,R0)，泛洪区域上界为（B0+upDiff1,G0+upDiff2,R0+upDiff3）
        
        #mask必须行和列都加2，且必须为uint8单通道阵列,为什么要加2可以这么理解：当从0行0列开始泛洪填充扫描时，mask多出来的2可以保证扫描的边界上的像素都会被处理
        mask = np.zeros([height+2,width+2],np.uint8)
        # mask_fill选择255白色，要移到8-15bit的位置，所以在flag中有(mask_fill<<8）
        mask_fill = 255
        #flags标志位是一个32bit的int类型数据，其由3部分组成： 0-7bit表示邻接性(4邻接、8邻接)；8-15bit表示mask的填充颜色；16-31bit表示填充模式（详见填充模式解释）
        #(1)Search from neighboring 8 connecting pixels instead of default 4;
        #(2)Only return the flood fill results in the mask image and do not modify the input image.
        flags = 8|(mask_fill<<8)|cv2.FLOODFILL_MASK_ONLY
        cv2.floodFill(frame, mask, seedPoint = seed, newVal = (255, 0, 0), 
            loDiff=(3,3,3), upDiff = (3,3,3),flags = flags)

            
        # Augment the illustration of the seed point
        cv2.circle(frame, seed, 2, (0, 0, 255), cv2.FILLED, cv2.LINE_AA)

        output.write(frame)

        #cv2.imshow('Road', frame)
        cv2.imshow('Mask', mask)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
finally:
    grabber.release()
    output.release()
    cv2.destroyAllWindows()