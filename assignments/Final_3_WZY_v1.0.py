# MAKE CHANGES TO IMAGE PIXELS
# Use numpy functions to load the original lenna image (512-by-512 
# color image format). Then load another image of your national flag, such as from:
# https://cdn.countryflags.com/download/china/flag-png-icon-64.png
# Please program a code that replaces pixels values from the top right 
# corner of the lenna image with those from the full color image of the 
# national flag image, and display the modified lenna image. Note that 
# after the modification, the bigger image of lenna must include the full 
# image of the smaller national flag image.

#需要使用的库
from matplotlib import image
from matplotlib import pyplot
import os

# 读取文件信息
path = os.path.dirname(os.path.abspath(__file__))
#lenna文件
lenna = path + '/' + 'lenna.bmp'
#国旗文件
flag= path + '/' + 'china-flag-xs.jpg'

#读取lenna并显示
data1 = image.imread(lenna)
pyplot.imshow(data1)
pyplot.show()

#读取文件并显示
data2 = image.imread(flag)
pyplot.imshow(data2)
pyplot.show()

#复制lenna文件信息
plot_data = data1.copy()

#国旗的高与宽
h=167
w=250

#在lenna图片范围内(512*512)
for width in range(512-250,512):
    for height in range(167):
        #将lenna中的像素改为国旗中的像素
        plot_data[height][width] = [data2[height][width-512+250][0], data2[height][width-512+250][1], data2[height][width-512+250][2]]

#展示图像
pyplot.imshow(plot_data)
pyplot.show()