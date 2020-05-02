import os
from matplotlib import image
import hashlib
'''利用hash_mad5进行加密'''

path = os.path.dirname(os.path.abspath(__file__))###读取文件
filename = path + '/' + 'lenna1.bmp'
filename1 = path + '/' + 'lenna.bmp'
hash_md5 = hashlib.md5()

data = image.imread(filename)###利用md5加密
text = bytearray(data)
hash_md5.update(text)
print(hash_md5.hexdigest())

data1 = image.imread(filename1)###利用md5加密
text1 = bytearray(data1)
hash_md5.update(text1)
print(hash_md5.hexdigest())