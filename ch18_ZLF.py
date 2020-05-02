from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# Prepare the training and testing data


# Create kNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, l_train)

# classify 
l_result = knn.predict(X_test)
print('kNN Accuracy: ', np.sum(l_result == l_test)/len(l_test))

import numpy as np
import matplotlib.pyplot as plt

# Define two Gaussian models
mu0 = [1, 2]
sigma0 = 1
mu1 = [-3, 1]
sigma1 = 1.5


def Gaussian2D(mu, sigma, sample_count):
    # Please note that we use simplified model to have a scalar sigma for all dimentions
    x = np.random.normal(mu[0], sigma, sample_count)
    y = np.random.normal(mu[1], sigma, sample_count)
    return [x, y]

class_sample_count = 50
sample_0 = Gaussian2D(mu0, sigma0, class_sample_count)
label1 = ['red']*50
sample_1 = Gaussian2D(mu1, sigma1, class_sample_count)
label0 = ['blue']*50

sample_0.extend(sample_1)
label1.extend(label0)
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(sample_0,label1)

import numpy as np
import matplotlib.pyplot as plt

# describe an underlying linear separation model y = 3x - 2
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

# Display the two classes
plt.plot(x_sample_class_0, y_sample_class_0, '*r')
plt.plot(x_sample_class_1, y_sample_class_1, 'Db')

# Display the underlying model
x = np.arange(-6, 6, 0.1)
y = linear_model(x)
plt.plot(x, y, 'gray', linewidth = 3)

plt.show()