from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.abspath(__file__))
name = path + '/' + 'lenna.bmp'
name1 = path + '/' + 'china-flag-icon-64.png'
picture= image.imread(name)
picture1= image.imread(name1)

print('Image type is: ', type(picture1))
print('Image shape is: ', picture1.shape)
plot_picture = picture.copy()
plot_picture1 = picture1.copy()
for width in range(picture1.shape[1]):
    for height in range(picture1.shape[0]):
        plot_picture[height][511- picture1.shape[1] + width] = plot_picture1[height][width] * 255

pip.show()