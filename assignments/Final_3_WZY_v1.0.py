# MAKE CHANGES TO IMAGE PIXELS
# Use numpy functions to load the original lenna image (512-by-512 
# color image format). Then load another image of your national flag, such as from:
# https://cdn.countryflags.com/download/china/flag-png-icon-64.png
# Please program a code that replaces pixels values from the top right 
# corner of the lenna image with those from the full color image of the 
# national flag image, and display the modified lenna image. Note that 
# after the modification, the bigger image of lenna must include the full 
# image of the smaller national flag image.
from matplotlib import image
from matplotlib import pyplot
import os
# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
lenna = path + '/' + 'lenna.bmp'
flag= path + '/' + 'china-flag-xs.jpg'
data1 = image.imread(lenna)
pyplot.imshow(data1)
pyplot.show()
data2 = image.imread(flag)
pyplot.imshow(data2)
pyplot.show()
# Add some color boundaries to modify an image array
plot_data = data1.copy()
h=167
w=250
for width in range(512-250,512):
    for height in range(167):
        plot_data[height][width] = [data2[height][width-512+250][0], data2[height][width-512+250][1], data2[height][width-512+250][2]]
# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()