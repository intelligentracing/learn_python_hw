import cv2
import numpy as np
import os
from pathlib import Path

path = os.path.dirname(os.path.abspath(__file__))
filename = path + "/" +'lincoln.tif'

image = cv2.imread(filename)
#gaussian kernel 5*5，标准差取0
blur5 = cv2.GaussianBlur(image, (5, 5), 0)
blur3 = cv2.GaussianBlur(image, (3, 3), 0)
DoGim = blur5 - blur3

#cv2.threshold（原图像，进行分类的阈值，高于（低于）阈值时赋予的新值，一个方法这里选择的是黑白二值）
_, threshImage = cv2.threshold(DoGim, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("original", image)
cv2.imshow("After DoG Blurred", threshImage)
cv2.waitKey(0)