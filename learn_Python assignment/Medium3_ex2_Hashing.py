import os
from matplotlib import image
import hashlib

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
filename1 = path + '/' + 'lenna_flag.jpg'
data = image.imread(filename)


hash_md5 = hashlib.md5()
text = bytearray(data)
hash_md5.update(text)
print(hash_md5.hexdigest())

hash_md5_1 = hashlib.md5()#Gets an MD5 encryption algorithm object
data1 = image.imread(filename1)#
text1 = bytearray(data1)
hash_md5_1.update(text1)#Specify a byte array type data that needs to be encrypted
print(hash_md5_1.hexdigest())#Gets the encrypted hexadecimal string
