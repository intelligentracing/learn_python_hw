import numpy as np
#ex1
#3个自由度，两个平动自由度分别是x和y，和一个Yaw轴/（Z轴）转动自由度
alpha = input("Enter rotation degrees (alpha): ")
alpha = float(alpha) /180 * np.pi; beta = float(0) / 180 * np.pi; gamma = float(0) / 180 * np.pi

x,y,z = input("Enter translation (x y z): ").split()
tx, ty = input("Enter translation (tx ty): ").split()
#两个平动自由度，tx ,ty,tz = 0
T = np.stack((float(tx), float(ty), float(0)))
vectors = np.stack((x, y, z))
dim, num = vectors.shape
#只有一个转动自由度，所以只有一个Yaw轴旋转矩阵
Rz = np.array([[np.cos(alpha), -np.sin(alpha), 0],[np.sin(alpha), np.cos(alpha), 0],[0,0,1]])
Rx = np.array([[1,0,0],[0,1,0],[0,0,1]])
Ry = np.array([[1,0,0],[0,1,0],[0,0,1]])

rotation_result = Rx.dot(Ry.dot(Rz.dot(vectors)))
translation_result = np.add(rotation_result, T)

#ex2
from plyfile import PlyData
import numpy as np
from mayavi import mlab
import os

# Read the ply file (from range sensor)
path = os.path.dirname(os.path.abspath(__file__))
# filename = path + '/bunny_data/bunny/data/bun000.ply'
filename = path + '/bunny_data/bunny/reconstruction/bun_zipper.ply'
plydata = PlyData.read(filename)

# Import 3D point clouds from plydata
vertex = plydata['vertex']
(x, y, z) = (vertex[t] for t in ('x', 'y', 'z'))
mlab.points3d(x, y, z, color=(1, 0, 0), mode='point')
mlab.axes(x_axis_visibility = True, y_axis_visibility = True, z_axis_visibility = True)

# Perform motion transform
#只绕一个轴转动，没有平动所以都设为0
tx = 0
ty = 0
tz = 0
T = np.stack((float(tx), float(ty), float(tz)))
vectors = np.stack((x, y, z))
dim, num = vectors.shape
T = np.repeat(T[:,np.newaxis], num, 1)
#绕z轴旋转，画出8个bunny图，转角为360/8 = 45°
for i in range(1, 8):
     alpha = i * 45
     alpha = float(alpha) /180 * np.pi; beta = float(0) / 180 * np.pi; gamma = float(0) / 180 * np.pi
     #alpha是Yaw轴转角，其他轴没有转动，所以beta,gamma角设置为0
     Rz = np.array([[np.cos(alpha), -np.sin(alpha), 0],[np.sin(alpha), np.cos(alpha), 0],[0,0,1]])
     Ry = np.array([[np.cos(beta), 0, np.sin(beta)],[0,1,0], [-np.sin(beta), 0, np.cos(beta)]])
     Rx = np.array([[1,0,0], [0, np.cos(gamma), -np.sin(gamma)],[0, np.sin(gamma), np.cos(gamma)]])
     rotation_result = Rx.dot(Ry.dot(Rz.dot(vectors)))
     translation_result = np.add(rotation_result, T)

     # New plot
     mlab.points3d(translation_result[0,:], translation_result[1,:],translation_result[2,:],\
          color=(0, 0, 1), mode='point')
mlab.show()