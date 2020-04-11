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

# Initialize the cursor input
cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'green', linewidth=2.0)

# Initialize the A and b matrices
A = np.zeros((2,2))
b = np.ones(2)
ob_count = 0
theta = np.arange(0, np.pi*2, 0.1)
x_sample=[]
y_sample=[]

def onclick(event):
    global ob_count, A, b, theta, x_sample,y_sample

    if ob_count==11:
        quit()

    [x, y] = [event.xdata, event.ydata]
    plt.plot(x, y, 'ro')

    # Update A and b
    if x>-10 and x<10 and y>-10 and y<10:
        x_sample.append(x**2);  y_sample.append(y**2)
        ob_count +=1
    
    if ob_count==10:
        A = np.zeros((ob_count, 2))
        for i in range(ob_count):
            A[i,0] = x_sample[i]
            A[i,1] = 1.0

        aa = np.linalg.lstsq(A, np.array(y_sample), rcond = None)[0]

        # Plot the ellipse
        if aa[0]<=0 or aa[1]<=0: # a^2, b^2 must be positive
            return
        b = math.sqrt(aa[1]); a = math.sqrt(-1/(aa[0]/b**2))
        x = a*np.cos(theta); y= b*np.sin(theta)
        plt.plot(x,y,'k-', linewidth = 3)

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()