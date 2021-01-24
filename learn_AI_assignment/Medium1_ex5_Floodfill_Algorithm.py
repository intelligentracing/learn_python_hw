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
       
        #(1)Search from neighboring 8 connecting pixels instead of default 4;
        # cv2.floodFill(img,mask,seed,newvalue(BGR),(loDiff1,loDiff2,loDiff3),(upDiff1,upDiff2,upDiff3),flag)
        # img：为待使用泛洪算法的图像
        # mask：为掩码层，使用掩码可以规定是在哪个区域使用该算法，如果是对于完整图像都要使用，则掩码层大小为原图行数+2，列数+2.
        #       是一个二维的0矩阵，边缘一圈会在使用算法是置为1。而只有对于掩码层上对应为0的位置才能泛洪，所以掩码层初始化为0矩阵。【dtype:np.uint8】
        # seed：为泛洪算法的种子点，也是根据该点的像素判断决定和其相近颜色的像素点，是否被泛洪处理。
        # newvalue：是对于泛洪区域新赋的值（B,G,R）
        # (loDiff1,loDiff2,loDiff3)：是相对于seed种子点像素可以往下的像素值，即seed(B0,G0,R0)，泛洪区域下界为（B0-loDiff1,G0-loDiff2,R0-loDiff3）
        # (upDiff1,upDiff2,upDiff3)：是相对于seed种子点像素可以往上的像素值，即seed(B0,G0,R0)，泛洪区域上界为（B0+upDiff1,G0+upDiff2,R0+upDiff3）
        # flag：为泛洪算法的处理模式。低八位 控制算法的连通性，是以seed点为中心，接着判断周围的几个像素点，再将泛洪区域像素点周围的几个像素点进行考虑。 一般为4，8；默认为4
        cv2.floodFill(frame, None, seedPoint = seed, newVal = (255, 0, 0), 
            loDiff=(3,3,3), upDiff = (3,3,3), flags = 8)
    

        #(2)Only return the flood fill results in the mask image and do not modify the input image.
        #mask必须行和列都加2，且必须为uint8单通道阵列,为什么要加2可以这么理解：当从0行0列开始泛洪填充扫描时，mask多出来的2可以保证扫描的边界上的像素都会被处理
        mask = np.zeros([height+2,width+2],np.uint8)
        # cv2.floodFill(frame, mask, seedPoint = seed, newVal = (255, 0, 0), 
        #     loDiff=(3,3,3), upDiff = (3,3,3),cv2.FLOODFILL_MASK_ONLY)

            
        # Augment the illustration of the seed point
        cv2.circle(frame, seed, 2, (0, 0, 255), cv2.FILLED, cv2.LINE_AA)

        output.write(frame)

        cv2.imshow('Road', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
finally:
    grabber.release()
    output.release()
    cv2.destroyAllWindows()