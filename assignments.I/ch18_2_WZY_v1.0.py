import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

#初始化图像
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
gxlist=[float("inf")]
gylist=[float("inf")]
times=10
best_learningrate=0

#列出方程
def func(x):
    return 1/4*x**4 + 1/3*x**3 - x**2 - 2

#求导后的方程(瞬时斜率)
def grad(x):
    return x**3 + x**2 - 2*x

#方程内容
x = np.arange(-5, 5, 0.1)
y = func(x)

#画出方程
plt.plot(x, y, 'c-', linewidth = 3)
line = None

#主方法
def onclick(event):
    global line ,gxlist,gylist,times,best_learningrate

    if not line == None:
        line.remove()
    epsilon = 0.001
    learn_rate =0.2
    delta = np.inf
    xlist = [event.xdata]  
    ylist = [func(event.xdata)]
    running_time=0
    while delta > epsilon and running_time<1000:
        #求出下一个x值,grad(xlist[-1])当前瞬时斜率
        x_next = xlist[-1] - learn_rate*grad(xlist[-1])
        #求出两个x值之间的差
        delta = abs(xlist[-1] - x_next)
        xlist.append(x_next)
        ylist.append(func(x_next))
        running_time+=1
    if ylist[-1]<gylist[-1]:
        gylist=ylist
        gxlist=xlist


    line, = plt.plot(gxlist, gylist, 'bo-')

cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'black')
fig.canvas.mpl_connect('button_press_event',onclick)

plt.show()