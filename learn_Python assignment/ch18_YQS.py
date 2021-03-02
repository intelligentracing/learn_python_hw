import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.patches import Ellipse
import math

#x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)等差数列函数（start，end, number)
#ex1.1
A = np.array([[1,0,1],[1,1,1],[1,-1,1]])
b = np.array([1,2,1]).T
n = b.shape[0]
#You need to determine if their rank corresponds to the full rank
# to make sure that you can find a solution
if np.linalg.matrix_rank(A) < n:
    print(np.linalg.matrix_rank(A),'<',n,)
    print('There are infinitely many solutions to this equation')
else:
    Ainv = np.linalg.inv(A)
    x = Ainv.dot(b)
    print('The solution of linear equation  =', x)


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

    # Initialize the cursor input
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
#x²/a² + y²/b² = 1
#A = np.array([[x1**2，y1**2],[x2**2, y2**2]])

























import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
#ex1.1
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Function y = 1/4 x^4 + 1/3 x^3 - x^2 - 2
def func(x):
    return 1/4*x**4 + 1/3*x**3 - x**2 - 2

def grad(x):
    return x**3 + x**2 - 2*x

x = np.arange(-5, 5, 0.1)
y = func(x)

plt.plot(x, y, 'r-', linewidth = 3)
line = None
def onclick(event):
    global line

    if not line == None:
        line.remove()

    x1 = event.xdata#用户点的点的横坐标
    value = func(x1)
    epsilon = 0.001
    learn_rate = [0.2, 0.02, 8,0.05]#将学习率改为一组数组
    delta = value
    iter = 0
    max_iteration = 10
    while delta > epsilon and iter < max_iteration:
        delta1 = 0
        x_next = x1
        for rate in learn_rate:
            '''比较不同学习率，选取可以使delta变化最快的学习率，
                这个for循环只为走一步'''
            x_try = x1 - rate*grad(x1)
            value_next = func(x_try)
            if value_next < value and value - value_next > delta1:#只有它的y值比用户点的点靠下以及新点与原点的距离比delta1更大，
                                                                 # 才说明新点比上一步更靠下，更靠近最小值
                delta1 = value -value_next#delta是新产生的下降点与原点之间的距离
                x_next = x_try
        if(x_next ==x1).all():
            break

        plt.plot([x1, x_next],[func(x1), func(x_next)], 'ko-')
        delta =np.linalg.norm(x1 - x_next)#更新delta，这里的delta是为了判断是否结束查找，与delta1不是一个数
        x1 = x_next
        iter += 1

cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'green')
fig.canvas.mpl_connect('button_press_event',onclick)

plt.show()

#ex1.2
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Function y = 1/4 x^4 + 1/3 x^3 - x^2 - 2
def func(x):
    return 1/4*x**4 + 1/3*x**3 - x**2 - 2

def grad(x):
    return x**3 + x**2 - 2*x

x = np.arange(-5, 5, 0.1)
y = func(x)

plt.plot(x, y, 'r-', linewidth = 3)

epsilon = 0.001
learn_rate = 0.1
delta = np.inf
sample_count = 10
x_sample = 8*np.random.random(sample_count)-4#将初始值变成（-4，4）之间的随机数
print(x_sample)
result_x_list = [np.inf]
result_y_list = [np.inf]
for x1 in x_sample:
    xlist = [x1]
    ylist = [func(x1)]

    while delta > epsilon:
        x_next = xlist[-1] - learn_rate*grad(xlist[-1])#这里要注意x_sample取值如果过小，比如小于-4，最后func(x)值会越来愈大，
                                                       # 且增长速度成指数级增长，最后发散，不会收敛，所以初值选取要注意
        delta = abs(xlist[-1] - x_next)#用横坐标值差值大小来判断是否结束循环
        xlist.append(x_next)
        ylist.append(func(x_next))

    if ylist[-1]< result_y_list[-1]:
        result_x_list = xlist
        result_y_list = ylist


line, = plt.plot(result_x_list, result_y_list, 'bo-',linewidth = 2)
print(result_y_list)

plt.show()