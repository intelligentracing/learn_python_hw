import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
#ex1.1
#describe an underlying linear separation model y = 3x - 2
def linear_model(x):
    return 3*x - 2

# generate two classes that are separable by the linear model

class_sample_count = 25  # Generate 10 samples in Class 0 and 10 in Class 1
x_sample_class_0 = 10 * np.random.random(class_sample_count) - 5
x_sample_class_1 = 10 * np.random.random(class_sample_count) - 5
y_sample_class_0 = linear_model(x_sample_class_0)+ 25*np.random.random(class_sample_count)
y_sample_class_1 = linear_model(x_sample_class_1) - 25*np.random.random(class_sample_count)
y_sample = np.append(y_sample_class_0, y_sample_class_1)
x_sample = np.append(x_sample_class_0, x_sample_class_1)
#创建数据集
X = np.zeros((50,2))
for i in range(50):
    X[i] = [x_sample[i],y_sample[i]]

#创建label集，因为X里面的数据是按照顺序排的，所以我们只需要把前25个设为0，后25个设为1即可，这样就完成了分两类的任务
l = np.zeros(50)

for i in range(len(X)):
    if i < 25:
        l[i] = 0
    if i >= 25:
        l[i] = 1
#随机把X,l分成测试集和训练集
x_train, x_test,l_train, l_test = train_test_split(X, l, test_size=0.5)


#在训练集上训练
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(x_train,l_train)

# classify
#在测试集上测试，这里只输入数据集x_test，然后获得它预测的label，与我们提前已经分类好的x_test的label也就是l_test进行比较，然后得出它是否分类正确的结果
l_result = knn.predict(x_test)
print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))

# Display the two classes
plt.plot(x_sample_class_0, y_sample_class_0, '*r')
plt.plot(x_sample_class_1, y_sample_class_1, 'Db')

plt.show()

#ex1.2

# Define two Gaussian models
mu0 = [1, 2]
sigma0 = 1
mu1 = [-3, 1]
sigma1 = 1.5


def Gaussian2D(mu, sigma, sample_count):
    # Please note that we use simplified model to have a scalar sigma for all dimentions
    x = np.random.normal(mu[0], sigma, sample_count)
    y = np.random.normal(mu[1], sigma, sample_count)
    return (x, y)


class_sample_count = 50
x_sample_0, y_sample_0 = Gaussian2D(mu0, sigma0, class_sample_count)
x_sample_1, y_sample_1 = Gaussian2D(mu1, sigma1, class_sample_count)
#创建数据集
X = np.zeros((100,2))
for i in range(50):
    X[i] = [x_sample_0[i],y_sample_0[i]]
for m in range(50):
    X[50 + m] = [x_sample_1[m],y_sample_1[m]]
#创建label集，因为X里面的数据是按照顺序排的，所以我们只需要把前50个设为0，后50个设为1即可，这样就完成了分两类的任务
l = np.zeros(100)
for i in range(len(X)):
    if i < 50:
        l[i] = 0
    if i >= 50:
        l[i] = 1
#随机把X,l分成测试集和训练集
x_train, x_test,l_train, l_test = train_test_split(X, l, test_size=0.5)
knn = KNeighborsClassifier(n_neighbors = 1)
#在训练集上训练
knn.fit(x_train,l_train)

# classify
#在测试集上测试，这里只输入数据集x_test，然后获得它预测的label，与我们提前已经分类好的x_test的label也就是l_test进行比较，然后得出它是否分类正确的结果
l_result = knn.predict(x_test)
print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))


fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.plot(x_sample_0, y_sample_0, 'r*')
plt.plot(x_sample_1, y_sample_1, 'bD')
plt.show()