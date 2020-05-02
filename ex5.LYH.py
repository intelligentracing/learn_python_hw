import os
from matplotlib import image
import hashlib

path = os.path.dirname(os.path.abspath(__file__))
md5 = hashlib.md5()
filename = path + '/' + 'lenna.bmp'
filename1 = path + '/' + 'lenna_flag.jpg'


