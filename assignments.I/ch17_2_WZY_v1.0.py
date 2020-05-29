import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.patches import Ellipse
import math

fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'black', linewidth=1.0)

A = np.zeros((2,2))
b = np.ones(2)
ob_count = 0
theta = np.arange(0, np.pi*2, 0.1)
x_sample=[]
y_sample=[]

def onclick(event):
    global ob_count, A, b, theta, x_sample,y_sample

    if ob_count == 10:
        quit()

    [x, y] = [event.xdata, event.ydata]
    x_sample.append(x)
    y_sample.append(y)
    plt.plot(x, y, 'co')
    ob_count += 1

    if ob_count == 10:
        x_sample_array = np.array(x_sample)
        y_sample_array = np.array(y_sample)
        A = np.zeros((ob_count, 2))
        for i in range(ob_count):
            A[i, 0] = x_sample_array[i] * x_sample_array[i]
            A[i, 1] = 1.0
            y_sample_array[i] = y_sample_array[i]*y_sample_array[i]

        aa = np.linalg.lstsq(A, y_sample_array, rcond=None)[0]
        if aa[0] >= 0 or aa[1] <= 0: 
            raise ValueError
        a = math.sqrt(-aa[1]/aa[0])
        b = math.sqrt(aa[1])
        x1 = a * np.cos(theta)
        y1 = b * np.sin(theta)
        l2, = plt.plot(x1, y1, 'b', linewidth=3)

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()