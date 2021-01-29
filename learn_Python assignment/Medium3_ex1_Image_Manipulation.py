from matplotlib import image
from matplotlib import pyplot
import os
from PIL import Image

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
flag = path + '/' + 'china-flag-png-large.png'
data = image.imread(filename)
data1 = image.imread(flag,0)

# Display image information
print('Image type is: ', type(data1))
print('Image shape is: ', data1.shape)
#print(data1)

# Add some color boundaries to modify an image array
plot_data = data.copy()
for width in range(data1.shape[1]):
    for height in range(data1.shape[0]):
        plot_data[height][511- data1.shape[1] + width] = data1[height][width] * 255

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()
#from array turn to image
image_output = Image.fromarray(plot_data)
image_output.save('lenna_flag.jpg')


