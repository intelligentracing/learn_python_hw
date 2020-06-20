## This is course material for Introduction to Modern Artificial Intelligence
## Class 10 Example code: mse.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Create data
x_bias = 0

samples1 = np.random.multivariate_normal([5+x_bias, 0], [[1, 0],[0, 1]], 100)
labels1 = np.ones(100)*-1
samples2 = np.random.multivariate_normal([-5+x_bias, 0], [[1, 0],[0, 1]], 100)
labels2 = np.ones(100)

samples = np.concatenate((samples1, samples2 ), axis =0)
labels = np.concatenate((labels1, labels2 ), axis =0)
    
# Plot the data
plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_d(x):
    return(sigmoid(x)*(1-sigmoid(x)))

def mse(samples, labels, w1, w2):
    result = 0
    count = len(labels)
    for i in range(count):
        result = result + (sigmoid(w1*samples[i,0] + w2*samples[i,1]) - labels[i])**2
    
    result = result / count
    return result

def mse_gradient(samples, labels, w1, w2):
    result = np.zeros(2)
    count = len(labels)
    for i in range(count):
        state = w1*samples[i,0] + w2*samples[i,1]
        result[0] = result[0] + samples[i,0] * sigmoid_d(state)*(sigmoid(state) - labels[i])
        result[1] = result[1] + samples[i,1] * sigmoid_d(state)*(sigmoid(state) - labels[i])

    result = result / count * 2
    return result

# Plot the parameter space of a linear separation function
fig = plt.figure()
ax2 = fig.add_subplot(1,1,1, projection = '3d')
a_arr, b_arr = np.meshgrid(np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1) )
func_value = np.zeros(a_arr.shape)
for x in range(a_arr.shape[0]):
    for y in range(a_arr.shape[1]):
            func_value[x, y] = mse(samples, labels, a_arr[x, y], b_arr[x, y])
ax2.plot_surface(a_arr, b_arr, func_value, color = 'red', alpha = 0.8)
ax2.set_xlabel('w1 parameter')
ax2.set_ylabel('w2 parameter')
ax2.set_zlabel('mse(f(w1, w2))')

# Gradient descent
print('Start gradient descend ...')
ww = np.array([4, 4])
ax2.scatter(ww[0], ww[1], mse(samples, labels, ww[0],ww[1]), 'r*')
delta = np.inf
epsilon = 0.0001
learn_rate = 5
step_count = 0
# Update vector aa
while delta > epsilon:
    gradient = mse_gradient(samples, labels, ww[0], ww[1])
    ww_next = ww - learn_rate * gradient
    ax2.plot([ww[0],ww_next[0]],[ww[1], ww_next[1]],\
        [mse(samples, labels, ww[0],ww[1]), mse(samples, labels, ww_next[0],ww_next[1]) ], 'ko-')
    delta = np.linalg.norm(ww - ww_next)
    ww = ww_next
    step_count +=1
    
ax2.scatter(ww[0], ww[1], mse(samples, labels, ww[0],ww[1]), 'r*')
plt.show()
print('Found parameters: {}'.format(ww))
print('Step Count:', step_count)