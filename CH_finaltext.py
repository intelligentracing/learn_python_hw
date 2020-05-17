import os
from matplotlib import image
import hashlib

hash_md5 = hashlib.md5()
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
filename1 = path + '/' + 'lenna_flag.jpg'

data = image.imread(filename)
text = bytearray(data)
hash_md5.update(text)
print(hash_md5.hexdigest())
 
hash_md6 = hashlib.md5()
data1 = image.imread(filename1)
text1 = bytearray(data1)
hash_md6.update(text1)
print(hash_md6.hexdigest())