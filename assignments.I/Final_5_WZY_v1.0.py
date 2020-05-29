# MD5 HASH FUNCTION
# Make use of the hashlib.md5() function, please code a program to 
# output the hexdigest() string of the lenna.bmp file and the modified 
# lenna plus national flag file.
# Note: Recall md5.update() takes only byte coded string or character 
# types. Therefore, a pixel of value between 0-255 needs to be coded as 
# a byte array before used in md5.update() input. A useful function to 
# do that is bytearray().

import hashlib
from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
lenna = path + '/' + 'lenna.bmp'
flag= path + '/' + 'china-flag-xs.jpg'
data1 = image.imread(lenna)
data2 = image.imread(flag)
# Add some color boundaries to modify an image array
plot_data = data1.copy()
for width in range(512-250,512):
    for height in range(167):
        plot_data[height][width] = [data2[height][width-512+250][0], data2[height][width-512+250][1], data2[height][width-512+250][2]]
# use pyplot to plot the image
dt1=bytearray(data1)
dt2=bytearray(plot_data)
print(hashlib.md5(dt1).hexdigest())
print(hashlib.md5(dt2).hexdigest())