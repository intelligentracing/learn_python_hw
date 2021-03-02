import matplotlib.pyplot as plt
import numpy as np
f#rom datetime import datetime
import os


#ex1.1
fig, ax = plt.subplots()
ax.spines['left'].set_position(('data',0))#将横纵坐标对齐
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#第一个正方形的横坐标数组
x0 = np.array([4,7,7,4,4])
y0 = np.array([0,0,3,3,0])
plt.plot(x0, y0, color = 'r', linewidth = 2)

#第二个正方形的横坐标数组
x1 = np.array([7,7,11,11,7])
y1 = np.array([3,7,7,3,3])
plt.plot(x1, y1, 'b', linewidth = 1)

#第三个正方形的横坐标数组
x2 = np.array([4,7,3,0,4])
y2 = np.array([3,7,10,6,3])
plt.plot(x2, y2, 'y', linewidth = 3)

#使横纵坐标单位长度统一
plt.axis('scaled')
plt.xticks(np.arange(0,12,2))
plt.yticks(np.arange(0,12,2))
plt.show()

















