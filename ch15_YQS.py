import numpy as np
import matplotlib.pyplot as plt
import math
#ex1.1

def rotationMatrix(degree):
    '''逆时针旋转角度的函数
    output:是旋转矩阵'''
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

input_times = input('按照XX:XX的时间格式输入任意时间：')
#input_times是字符串格式，将其中的时间用spilt函数提取出来
input_times_spilt = input_times.split(':')
hours = int(input_times_spilt[0])#从字符串变成整数格式
minutes = int(input_times_spilt[1])
hours_degree = 360 - (30 * (hours + minutes/60))#时针旋转的角度，因为旋转矩阵是逆时针旋转的，所以需要用360减去它
minutes_degree = 360 - (6 * minutes)#分针旋转的角度
#时针和分针原本的向量，他们在x,y坐标系下表示竖直向上长度分别为1和2
v1 = np.array([0.,1.])
v2 = np.array([0.,2.])
rotation_hours = rotationMatrix(hours_degree)
rotation_minutes = rotationMatrix(minutes_degree)
#旋转矩阵点乘原来的向量得到的向量，就是按照我们计算出的角度，旋转后的的向量
v1_new = rotation_hours.dot(v1)
v2_new = rotation_minutes.dot(v2)
#打印结果
plt.arrow(0,5,v1_new[0],v1_new[1], head_width=0.4, head_length=0.4, color = 'b')
plt.arrow(0,5,v2_new[0],v2_new[1],head_width=0.4, head_length=0.4, color = 'r')
plt.axis([-5,5,0,10])
plt.show()

#ex1.2
#(1)将它的[:2,:2] 的子矩阵复制，得到的矩阵为：[[7,8],[1,3]]
a = np.array([[7,8,8],[1,3,8],[9,2,1]])
new_matrix = a[:2,:2].copy()
#(2)子矩阵的每一列代表的向量的长度归为一： sqrt(x0*x0 + x1*x1) = 1， 而方向不变，例：7/math.sqrt(7**2 + 1**2)
new_matrix_cut = np.ones((2,2))
new_matrix_cut[0,0] = new_matrix[0,0]/math.sqrt(new_matrix[0,0]**2 + new_matrix[1,0]**2)
new_matrix_cut[1,0] = new_matrix[1,0]/math.sqrt(new_matrix[0,0]**2 + new_matrix[1,0]**2)
new_matrix_cut[0,1] = new_matrix[0,1]/math.sqrt(new_matrix[0,1]**2 + new_matrix[1,1]**2)
new_matrix_cut[1,1] = new_matrix[1,1]/math.sqrt(new_matrix[0,1]**2 + new_matrix[1,1]**2)
#(3)）用一个旋转顺时针 90 度的 rotation matrix 点乘这个子矩阵，打 印结果。
def rotationMatrix(degree):
    '''逆时针旋转角度的函数'''
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

rotation_matrix = rotationMatrix(270)#生成旋转矩阵
new_matrix_dot = rotation_matrix.dot(new_matrix_cut)#与需要旋转的矩阵点乘
print(new_matrix_dot)

#(4)用 pyplot 对（2） 中的变换之前和之后的向量进行图像显示

#归一化之前
plt.arrow(0,0,new_matrix[0,0],new_matrix[1,0], head_width=0.4, head_length=0.4, color = 'b')
plt.arrow(0,0,new_matrix[0,1],new_matrix[1,1], head_width=0.4, head_length=0.4, color = 'b')
#归一化之后
plt.arrow(0,0,new_matrix_cut[0,0],new_matrix_cut[1,0], head_width=0.4, head_length=0.4, color = 'r')
plt.arrow(0,0,new_matrix_cut[0,1],new_matrix_cut[1,1], head_width=0.4, head_length=0.4, color = 'r')
plt.axis([0,10,0,10])
plt.show()
#(4)用 pyplot 对（3） 中的变换之前和之后的向量进行图像显示
plt.figure()#擦除上一个图
#坐标旋转前new_matrix_cut
plt.arrow(5,0,new_matrix_cut[0,0],new_matrix_cut[1,0], head_width=0.4, head_length=0.4, color = 'b')
plt.arrow(5,0,new_matrix_cut[0,1],new_matrix_cut[1,1], head_width=0.4, head_length=0.4, color = 'b')
#坐标旋转后new_matrix_dot
plt.arrow(5,0,new_matrix_dot[0,1],new_matrix_dot[1,1], head_width=0.4, head_length=0.4, color = 'r')
plt.arrow(5,0,new_matrix_dot[0,0],new_matrix_dot[1,0], head_width=0.4, head_length=0.4, color = 'r')
plt.axis([0,10,-5,5])
plt.show()