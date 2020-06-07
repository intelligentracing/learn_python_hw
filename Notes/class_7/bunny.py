## This is course material for Introduction to Modern Artificial Intelligence
## Class 7 Example code: bunny.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use
#
# Copyright (c) 2014-2015, Enthought, Inc.
# Standard library imports
import os
from os.path import join
# Please make sure to conda install -c conda-forge mayavi
from mayavi import mlab

path = os.path.dirname(os.path.abspath(__file__))

# Extract the data
import tarfile
#打开压缩文件
bunny_tar_file = tarfile.open(path+'/bunny.tar.gz')
#尝试以下代码
try:
    #制作文件路径
    os.mkdir(path+'/bunny_data')
    #解压并保存到文件夹
    bunny_tar_file.extractall(path+'/bunny_data')
    #关闭窗口
    bunny_tar_file.close()
except:
    pass

# Path to the bunny ply file
bunny_ply_file = join('bunny_data', 'bunny', 'reconstruction', 'bun_zipper.ply')

# Render the bunny ply file
mlab.pipeline.surface(mlab.pipeline.open(bunny_ply_file))
mlab.show()