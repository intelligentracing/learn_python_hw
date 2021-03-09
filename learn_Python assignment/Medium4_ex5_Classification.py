import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from math import exp
from math import pi
from scipy.stats import multivariate_normal
# the first model
mu0 = [1, 2]
sigma0 = 1
#the second model
mu1 = [-3, 1]
sigma1 = 1.5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
x_sample_0 = []
y_sample_0 = []
x_sample_1 = []
y_sample_1 = []


# For every point at coordinates [x, y], evaluate its probability with respect 
#to Model 0 and Model 1, and perform the classification.
def proability(x, y):
    #根据两组mu 和 sigma值构建两个类别
    proability0 = 1 / (2 * np.pi* sigma0)*np.exp(((x - mu0[0])**2 + (y - mu0[1])**2) / (2*sigma0**2))
    proability1 = 1 / (2 * np.pi * sigma1) * np.exp(((x - mu1[0]) ** 2 + (y - mu1[1]) ** 2) / (2 * sigma1 ** 2))
    if proability0 > proability1:
        #x:数据，y:要保留的小数点位数
        x_sample_0.append(round(x,1))
        y_sample_0.append(round(y,1))
    plt.scatter(x_sample_0,y_sample_0,color = 'red',s = 0.1)

    if proability1 > proability0: 
        x_sample_1.append(round(x, 1))
        y_sample_1.append(round(y, 1))
    plt.scatter(x_sample_1, y_sample_1, color = 'blue', s = 0.1)
#(1) Use numpy.meshgrid() to generate a grid of samples between -5 and 5 for both X axis and Y axis and use stepsize = 0.1.
x_rr,y_rr = np.meshgrid(np.arange(-5,5,0.1),np.arange(-5,5,0.1))


for i in range(len(x_rr[0])):
    for j in range(len(y_rr[0])):
        proability(x_rr[i][j],y_rr[i][j])

plt.show()

#######3D display#######

# #x.flat: Return a copy of the array collapsed into one dimension.
# #np.column_stack将两个矩阵合并
# xy = np.column_stack([x_rr.flat, y_rr.flat])
# means = np.array([-3, 1])
# sigma = np.array([1.5, 1.5])
# #当 np.diag(array) 中
# #array是一个1维数组时，结果形成一个以一维数组为对角线元素的矩阵
# #array是一个二维矩阵时，结果输出矩阵的对角线元素
# covariance = np.diag(sigma**2)
# # multivariate_normal.pdf生成多元正态分布
# #multivariate_normal.pdf（依据的坐标点，均值，协方差）
# z = multivariate_normal.pdf(xy, mean=means, cov=covariance)
# z = z.reshape(x_rr.shape)
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111, projection='3d')
# ax2.plot_surface(x_rr,y_rr,z)
# plt.show()



# x,y = list(np.arange(-5,10,0.1)), list(np.arange(-5,10,0.1))
# red_group = ([],[])
# blue_group = ([],[])
# for i in range(len(x)):
#     for j in range(len(y)):
#         if normal_value(x[i],y[j],1,2,1) >= normal_value(x[i],y[j],-3,1,1.5):
#             red_group[0].append(x[i])
#             red_group[1].append(y[j])
#         else:
#             blue_group[0].append(x[i])
#             blue_group[1].append(y[j])

# plt.scatter(red_group[0],red_group[1],color='red',s = 0.1)
# plt.scatter(blue_group[0],blue_group[1],color='blue',s=0.1)
# plt.show()