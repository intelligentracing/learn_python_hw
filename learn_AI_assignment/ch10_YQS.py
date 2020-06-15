import numpy as np
import matplotlib.pyplot as plt

vectors_xw = np.stack((1, 0, 0,1))
vectors_yw = np.stack((0, 1, 0,1))
vectors_zw = np.stack((0, 0, 1,1))

alpha = float(90) /180 * np.pi; beta = float(90) / 180 * np.pi; gamma = float(90) / 180 * np.pi
Rz = np.array([[np.cos(alpha), -np.sin(alpha), 0],[np.sin(alpha), np.cos(alpha), 0],[0,0,1]])
Ry = np.array([[np.cos(beta), 0, np.sin(beta)],[0,1,0], [-np.sin(beta), 0, np.cos(beta)]])
Rx = np.array([[1,0,0], [0, np.cos(gamma), -np.sin(gamma)],[0, np.sin(gamma), np.cos(gamma)]])
R = Rx.dot(Ry.dot(Rz))


tx = 3; ty = 4; tz = 5
T = np.stack((float(tx), float(ty), float(tz)))
Tm = np.repeat(T[:, np.newaxis], 3, 1)
matrix0 = np.hstack((R, Tm))
matrix1 = matrix0[:,:4]
print(matrix1)
matrix2 = np.array([[0, 0, 0, 1],[0, 0, 0, 1],[0, 0, 0, 1]])

Extrinsic = np.vstack((matrix1,matrix2))
Extrinsic = Extrinsic[:4]
vectors_xc = Extrinsic.dot(vectors_xw)
vectors_yc = Extrinsic.dot(vectors_yw)
vectors_zc = Extrinsic.dot(vectors_zw)

#Q2
f = 40

ax = f / 0.1 ; ay = f /0.1 ; cx = 5 ; cy = 5
Intrinsic = np.array([[ax, 0, 0], [0, ay, cy],[0, 0, 1]])
vectors_xuv = Intrinsic.dot(matrix1.dot(vectors_xw))
vectors_yuv = Intrinsic.dot(matrix1.dot(vectors_yw))
vectors_zuv = Intrinsic.dot(matrix1.dot(vectors_zw))


dxx = vectors_xuv[0] / 6
dyx = vectors_xuv[1] / 6
dxy = vectors_yuv[0] / 6
dyy = vectors_yuv[1] / 6
dxz = vectors_zuv[0] / 6
dyz = vectors_zuv[1] / 6
plt.xlim((0,1000))
plt.ylim((0, 1000))
plt.arrow(0, 0, dxx, dyx)
plt.arrow(0,0, dxy, dyy)
plt.arrow(0,0, dxz, dyz)
plt.show()
print('Xw axis unit in Xc ,Xc = ',vectors_xc, 'Yw axis unit in Yc ,Yc = ', vectors_yc, 'Zw axis unit in Zc ,Zc = ', vectors_zc,end='')