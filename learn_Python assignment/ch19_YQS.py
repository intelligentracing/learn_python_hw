import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
#ex1.1 Using adaptive descent to test multiple learning rates.
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
    #将学习率改为一组数组
    learn_rate = [0.2, 0.02, 8,0.05]
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
            # 只有它的y值比用户点的点靠下以及新点与原点的距离比delta1更大，
            # 才说明新点比上一步更靠下，更靠近最小值
            if value_next < value and value - value_next > delta1:
                delta1 = value -value_next#delta是新产生的下降点与原点之间的距离
                x_next = x_try
        #sainty check whether the next step is refreshing
        if(x_next == x1).all():
            break

        plt.plot([x1, x_next],[func(x1), func(x_next)], 'go-')
        #更新delta，这里的delta是为了判断是否结束查找，与delta1不是一个数
        delta =np.linalg.norm(x1 - x_next)
        x1 = x_next
        iter += 1

cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'green')
fig.canvas.mpl_connect('button_press_event',onclick)

plt.show()

#ex1.2 Using loops to select the optimal global solution from multiple initial values.
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
#将初始值变成（-4，4）之间的随机数
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













# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# #ex1.1
# #describe an underlying linear separation model y = 3x - 2
# def linear_model(x):
#     return 3*x - 2

# # generate two classes that are separable by the linear model

# class_sample_count = 25  # Generate 25 samples in Class 0 and 25 in Class 1
# x_sample_class_0 = 10 * np.random.random(class_sample_count) - 5 #convert the range from (0,1) to (-5,5)
# x_sample_class_1 = 10 * np.random.random(class_sample_count) - 5
# y_sample_class_0 = linear_model(x_sample_class_0)+ 25*np.random.random(class_sample_count)
# y_sample_class_1 = linear_model(x_sample_class_1) - 25*np.random.random(class_sample_count)
# y_sample = np.append(y_sample_class_0, y_sample_class_1)
# x_sample = np.append(x_sample_class_0, x_sample_class_1)
# #creating data sets
# X = np.zeros((50,2))
# for i in range(50):
#     X[i] = [x_sample[i],y_sample[i]]

# #Create the label set. Since the data in X is arranged in order, we only need to set the first 25 as 0 and the last 25 as 1,
# #thus completing the task divided into two categories
# l = np.zeros(50)

# for i in range(len(X)):
#     if i < 25:
#         l[i] = 0
#     if i >= 25:
#         l[i] = 1
# #Randomly divide X and L into test set and training set
# x_train, x_test,l_train, l_test = train_test_split(X, l, test_size=0.5)
 

# #Train on the training set
# #The sample point of the unknown classification belongs to the category of the point closest to the unknown classification sample point
# knn = KNeighborsClassifier(n_neighbors = 2 )
# knn.fit(x_train,l_train)

# # classify
# #Test on the test set, where you just enter the data set x_test and get the label it predicts,
# # then compare with the l_test,And then determine if it's classified correctly
# #在测试集上测试，这里只输入数据集x_test，然后获得它预测的label，与我们提前已经分类好的x_test的label也就是l_test进行比较，然后得出它是否分类正确的结果
# l_result = knn.predict(x_test)
# print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))

# # Display the two classes
# plt.plot(x_sample_class_0, y_sample_class_0, 'r*')
# plt.plot(x_sample_class_1, y_sample_class_1, 'Db')

# plt.show()

# #ex1.2

# #Define two Gaussian models
# mu0 = [1, 2]
# sigma0 = 1
# mu1 = [-3, 1]
# sigma1 = 1.5


# def Gaussian2D(mu, sigma, sample_count):
#     # Please note that we use simplified model to have a scalar sigma for all dimentions
#     x = np.random.normal(mu[0], sigma, sample_count)
#     y = np.random.normal(mu[1], sigma, sample_count)
#     return (x, y)


# class_sample_count = 50
# x_sample_0, y_sample_0 = Gaussian2D(mu0, sigma0, class_sample_count)
# x_sample_1, y_sample_1 = Gaussian2D(mu1, sigma1, class_sample_count)

# #创建数据集
# X = np.zeros((100,2))
# for i in range(50):
#     X[i] = [x_sample_0[i],y_sample_0[i]]
# for m in range(50):
#     X[50 + m] = [x_sample_1[m],y_sample_1[m]]
# #创建label集，因为X里面的数据是按照顺序排的，所以我们只需要把前50个设为0，后50个设为1即可，这样就完成了分两类的任务
# l = np.zeros(100)
# for i in range(len(X)):
#     if i < 50:
#         l[i] = 0
#     if i >= 50:
#         l[i] = 1
# #随机把X,l分成测试集和训练集
# x_train, x_test,l_train, l_test = train_test_split(X, l, test_size=0.5)
# knn = KNeighborsClassifier(n_neighbors = 1)
# #在训练集上训练
# knn.fit(x_train,l_train)

# # classify
# #在测试集上测试，这里只输入数据集x_test，然后获得它预测的label，与我们提前已经分类好的x_test的label也就是l_test进行比较，然后得出它是否分类正确的结果
# l_result = knn.predict(x_test)
# print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.spines['left'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.plot(x_sample_0, y_sample_0, 'r*')
# plt.plot(x_sample_1, y_sample_1, 'bD')
# plt.show()