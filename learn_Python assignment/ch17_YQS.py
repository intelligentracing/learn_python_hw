import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.patches import Ellipse
import math

#x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)等差数列函数（start，end, number)
#ex1.1
# A = np.array([[1,0,1],[1,1,1],[1,-1,1]])
# b = np.array([1,2,1]).T
# n = b.shape[0]
# #You need to determine if their rank corresponds to the full rank to make sure that you can find a solution
# if np.linalg.matrix_rank(A) < n:
#     print(np.linalg.matrix_rank(A),'<',n,)
#     print('There are infinitely many solutions to this equation')
# else:
#     Ainv = np.linalg.inv(A)
#     x = Ainv.dot(b)
#     print('The solution of linear equation  =', x)

#ex1.2


#Initialize the figure and axes
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
#（1）Set a = 4, b = 2, print the model of the ellipse in the 2d diagram, and mark it as gray color.
a = 4
b = 2
#A polar expression for an elliptic equation
theta = np.arange(0, np.pi * 2, 0.1)
x = a * np.cos(theta)
y = b * np.sin(theta)
l1, = plt.plot(x, y, 'gray', linewidth=2)

# # Initialize the cursor input
cursor = Cursor(ax, horizOn=True, vertOn=True, color='g', linewidth=2.0)#画十字线
ob_count = 0
x_sample = []#In order to place the points that we drew near the ellipse
y_sample = []


def onclick(event):
    global ob_count

    # if ob_count == 10:
    #     quit()
    #(2)append Cursor widget，The user clicks 10 points around the ellipse, which can be noisy, that is,
    # may be off the ellipse line
    [x, y] = [event.xdata, event.ydata]
    x_sample.append(x)
    y_sample.append(y)
    plt.plot(x, y, 'ro')#display the dot
    ob_count += 1

    if ob_count == 10:
        x_sample_array = np.array(x_sample)
        y_sample_array = np.array(y_sample)
        # Initialize the A matrix，convert the ellipse function form to  y = ax + b, that means：-a²/b² * x² + b² = y²，It's going to be Ax = b
        #A matrix [x², 1]，X matrix [-a²/b² ,b²],b is y²
        A = np.zeros((ob_count, 2))
        b = np.zeros(ob_count)

        for i in range(ob_count):
            A[i, 0] = x_sample_array[i] * x_sample_array[i]
            A[i, 1] = 1.0
            b[i] = y_sample_array[i] * y_sample_array[i]

        #Use the least square method to find the x matrix
        aa = np.linalg.lstsq(A, b, rcond=None)[0]
        if aa[0] >= 0 or aa[1] <= 0:  # a^2, b^2 must be positive
            raise ValueError('This is wrong!')
        
        #Find a and b in the elliptic equation
        a = math.sqrt(-1/aa[0] * aa[1])
        b = math.sqrt(aa[1])
        #polar expression for an elliptic equation
        x1 = a * np.cos(theta)
        y1 = b * np.sin(theta)
        #display the ellipse
        l2, = plt.plot(x1, y1, 'r', linewidth=1)
        plt.show()

#respond for keyboard input，print the input value
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()