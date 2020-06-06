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
tx, ty, tz = input("Enter translation (tx ty tz): ").split()
T = np.stack((float(tx), float(ty), float(tz)))
alpha, beta, gamma = input("Enter rotation degrees (alpha beta gamma): ").split()
alpha = float(alpha) /180 * np.pi; beta = float(beta) / 180 * np.pi; gamma = float(gamma) / 180 * np.pi

vectors = np.stack((x, y, z))
dim, num = vectors.shape
Tm = np.repeat(T[:,np.newaxis], num, 1)
Rz = np.array([[np.cos(alpha), -np.sin(alpha), 0],[np.sin(alpha), np.cos(alpha), 0],[0,0,1]])
Ry = np.array([[np.cos(beta), 0, np.sin(beta)],[0,1,0], [-np.sin(beta), 0, np.cos(beta)]])
Rx = np.array([[1,0,0], [0, np.cos(gamma), -np.sin(gamma)],[0, np.sin(gamma), np.cos(gamma)]])
rotation_result = Rx.dot(Ry.dot(Rz.dot(vectors)))
translation_result = np.add(rotation_result, Tm)

# New plot
mlab.points3d(translation_result[0,:], translation_result[1,:],translation_result[2,:],\
     color=(0, 0, 1), mode='point')
mlab.show()