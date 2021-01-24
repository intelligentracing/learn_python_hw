import cv2
import numpy as np
import os
# load file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/highway_video.mp4'
outputFilename = path + '/output_video.avi'

grabber = cv2.VideoCapture(filename)
fps = int(grabber.get(cv2.CAP_PROP_FPS))
width = int(grabber.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(grabber.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter(outputFilename, cv2.VideoWriter_fourcc('M', 'J', 'P','G'),\
     fps, (width, height), False)
smoothFilter = np.array([[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]])/ 159.0
while(grabber.isOpened()):
    ret, frame = grabber.read()


    if ret == False:
        break

    # Create gray image and denoise
    #gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #canny算子的blur kernel如下
    
    #用cv2.filter2D（）
    smoothImage = cv2.filter2D(frame, -1, smoothFilter)


    cv2.imshow('Edge Image', smoothImage)
    output.write(smoothImage)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

grabber.release()
output.release()
cv2.destroyAllWindows()