#1个自由度

## This is course material for Introduction to Modern Artificial Intelligence
## Class 7 Example code: rigid_body_motion.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to conda install -c conda-forge plyfile mayavi
from plyfile import PlyData
import numpy as np
from mayavi import mlab
import os

#文件读取
path = os.path.dirname(os.path.abspath(__file__))
#文件路径
filename = path + '/bunny_data/bunny/reconstruction/bun_zipper.ply'
#读取数据
plydata = PlyData.read(filename)


def bunny_rotation(degree, times):
     for i in range(times):
          #引入plyfile(点云中所有点的坐标)
          vertex = plydata['vertex']
          #取出x,y,z数值
          (x, y, z) = (vertex[t] for t in ('x', 'y', 'z'))
          #建立空间
          mlab.points3d(x, y, z, color=(1, 0, 0), mode='point')
          #确认xyz三轴
          mlab.axes(x_axis_visibility = True, y_axis_visibility = True, z_axis_visibility = True)
          #获取用户输入
          tx, ty, tz = 0,0,0
          #将用户输入转化为栈(只能计算浮点数才能计算)
          T = np.stack((float(tx), float(ty), float(tz)))
          #获取用户输入
          alpha, beta, gamma = degree[0]/times*i,degree[1]/times*i,degree[2]/times*i
          #角度转弧度
          alpha = float(alpha) /180 * np.pi; beta = float(beta) / 180 * np.pi; gamma = float(gamma) / 180 * np.pi
          #新建向量
          vectors = np.stack((x, y, z))
          #获取向量参数(维度(T的重复次数))
          dim, num = vectors.shape
          #生成多个矩阵用于相加(升维)
          Tm = np.repeat(T[:,np.newaxis], num, 1)
          #生成旋转矩阵
          Rz = np.array([[np.cos(alpha), -np.sin(alpha), 0],\
                         [np.sin(alpha), np.cos(alpha) , 0],\
                         [0            ,0              , 1]])
          Ry = np.array([[np.cos(beta)  , 0 , np.sin(beta)],\
                         [0             , 1 , 0           ],\
                         [-np.sin(beta) , 0 , np.cos(beta)]])
          Rx = np.array([[1, 0            ,0              ],\
                         [0, np.cos(gamma), -np.sin(gamma)],\
                         [0, np.sin(gamma), np.cos(gamma)]])
          #旋转
          rotation_result = Rx.dot(Ry.dot(Rz.dot(vectors)))
          #添加结果
          translation_result = np.add(rotation_result, Tm)
          #建立新的空间(画点)
          mlab.points3d(translation_result[0,:], translation_result[1,:],translation_result[2,:],\
               color=(0, 0, 1), mode='point')
               #展示
     mlab.show()

bunny_rotation([360,0,0], 8)