import numpy as np
import matplotlib.pyplot as plt
'''这个程序将通过运用高斯分布来计算点分布在两个方程中的可能性并进行比较与分类，并将分布结果以图像形式展示'''


u0 = [1,2]###两组方程的标准差与均值
o0 = 1
u1 = [-3,1]
o1 = 1.5

SampleList = []###基础数据：ListA为可能分布在0号方程的点的合集，ListB为可能分布在1号方程的点的集

ListA = []
ListB = []

x_rr,y_rr = np.meshgrid(np.arange(-5,5,1),np.arange(-5,5,1))

for i in range(len(x_rr[0])):
    for j in range(len(y_rr[0])):
        SampleList.append((x_rr[i][j],y_rr[i][j]))


def Gaussian(u,o,x,y):###利用二维正态分布计算可能性
    posibilty = (1/2*np.pi*o**2)*np.exp(((x - u[0])**2 + (y - u[1])**2) / (2*o**2))
    return posibilty

for a in SampleList:###比较可能性并进行分类
    if Gaussian(u0,o0,a[0],a[1])>Gaussian(u1,o1,a[0],a[1]):
        ListA.append(a)
    else:
        ListB.append(a)

fig = plt.figure()###生成图像
ax = fig.add_subplot(111)
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

for c in ListA:###打点，并以颜色进行区分
    plt.plot(c[0],c[1],'r*')
for c in ListB:
    plt.plot(c[0],c[1],'bD')

plt.show()###显示