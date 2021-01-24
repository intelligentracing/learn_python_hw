#ex2
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
output = cv2.VideoWriter(outputFilename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), \
                         fps, (width, height), True)

while (grabber.isOpened()):
    ret, frame = grabber.read()

    seed = (width // 2, height - 100)
    #mask = np.zeros([height + 2, width + 2],np.uint8)
    # 要求mask必须是大小为（height + 2，width + 2），但是只有在为0的区域才会进行floodfill，
    # 所以可以像如下所示先设置mask大小为（height + 2，width + 2）
    mask = np.ones([height + 2, width + 2, 1], np.uint8)
    # 然后再自己设置为0的区域
    mask[0 : height - 90, 0 : width] = 0
    # Flood the frame to segment only the road
    cv2.floodFill(frame, mask, seedPoint=seed, newVal=(255, 0, 0), loDiff=(3, 3, 3), upDiff=(3, 3, 3))

    # Augment the illustration of the seed point
    cv2.circle(frame, seed, 2, (0, 0, 255), cv2.FILLED, cv2.LINE_AA)

    output.write(frame)

    cv2.imshow('Road', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

grabber.release()
output.release()
cv2.destroyAllWindows()