##3.image processing
from matplotlib import image
from matplotlib import pyplot
import os
'''这段代码读取了lenna的图像和国旗的图像，并将国旗的图像融合在lenna图像的右上角。
输出：右上角被国旗覆盖的lenna图像'''

# 读取图像
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

path1 = os.path.dirname(os.path.abspath(__file__))
filename1 = path1 + '/' + 'flag'
data1 = image.imread(filename1)


# 将图像融合
for width in range(250):
    for height in range(167):
        date[height][511-width] = data1[height][width]

# 图像展示
pyplot.imshow(date)
pyplot.show()