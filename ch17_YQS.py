import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.patches import Ellipse
import math
#ex1.1
A = np.array([[1,0,1],[1,1,1],[1,-1,1]])
b = np.array([1,2,1])
n = b.shape[0]
#需要判断它们的秩是否符合满秩以确保是否能求出解
if np.linalg.matrix_rank(A) < n:
    print(np.linalg.matrix_rank(A),'<',n,'该方程无穷多解')
else:
    Ainv = np.linalg.inv(A)
    x = Ainv.dot(b)
    print('The solution of linear equation  =', x)

#ex1.2


Initialize the figure and axes
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
#（1）令 a = 4, b = 2，在二维图中打印椭圆的model， 并标记为gray颜色。
a = 4
b = 2
theta = np.arange(0, np.pi * 2, 0.1)
x = a * np.cos(theta)
y = b * np.sin(theta)
l1, = plt.plot(x, y, 'gray', linewidth=2)

# # Initialize the cursor input
cursor = Cursor(ax, horizOn=True, vertOn=True, color='g', linewidth=2.0)#画十字线
ob_count = 0
x_sample = []#为了放置我们在椭圆附近画的点
y_sample = []
x1 = np.arange(-5, 5, 0.1)

def onclick(event):
    global ob_count

    if ob_count == 10:
        quit()
    #(2)添加Cursor widget，使用户在椭圆形的周围点击10个点，这10个点可以是带噪音的，即可能脱离椭圆线
    [x, y] = [event.xdata, event.ydata]
    x_sample.append(x)
    y_sample.append(y)
    plt.plot(x, y, 'ro')#把点显示出来
    ob_count += 1

    if ob_count == 10:
        x_sample_array = np.array(x_sample)
        y_sample_array = np.array(y_sample)
        # 初始化A矩阵，将椭圆方程转换成y = ax + b的格式，即：-a²/b² * x² + b² = y²，化为Ax = b的矩阵格式
        #A矩阵为[x², 1]，x矩阵为[-a²/b² ,b²],b为y²
        A = np.zeros((ob_count, 2))
        for i in range(ob_count):
            A[i, 0] = x_sample_array[i] * x_sample_array[i]
            A[i, 1] = 1.0
            y_sample_array[i] = y_sample_array[i]*y_sample_array[i]

        #运用最小二乘法求x矩阵
        aa = np.linalg.lstsq(A, y_sample_array, rcond=None)[0]
        if aa[0] >= 0 or aa[1] <= 0:  # a^2, b^2 must be positive
            raise ValueError
        #求出椭圆方程中的a,b
        a = math.sqrt(-aa[1]/aa[0])
        b = math.sqrt(aa[1])
        #下式为椭圆的极坐标方程
        x1 = a * np.cos(theta)
        y1 = b * np.sin(theta)
        #画椭圆
        l2, = plt.plot(x1, y1, 'r', linewidth=1)
        plt.show()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()