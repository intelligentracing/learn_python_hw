## This is course material for Introduction to Modern Artificial Intelligence
## Class 11 Example code: mlp.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Load dependencies
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from keras.activations import sigmoid
#防止报错
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
# Create data
linearSeparableFlag = False
#激发函数校正
x_bias = 0
label1 = np.array([[1, 0]])
label2 = np.array([[0, 1]])
#若线性可分
if linearSeparableFlag:

    samples1 = np.random.multivariate_normal([5+x_bias, 0], [[1, 0],[0, 1]], 100)
    
    labels1 = np.repeat(label1, 100, axis = 0)

    samples2 = np.random.multivariate_normal([-5+x_bias, 0], [[1, 0],[0, 1]], 100)
    labels2 = np.repeat(label2, 100, axis = 0)

    samples = np.concatenate((samples1, samples2 ), axis =0)
    labels = np.concatenate((labels1, labels2 ), axis =0)
    # Plot the data
    plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
    plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
    plt.show()

else:
    samples1 = np.random.multivariate_normal([5+x_bias, 5], [[1, 0],[0, 1]], 50)
    samples2 = np.random.multivariate_normal([-5+x_bias, -5], [[1, 0],[0, 1]], 50)
    labels1 = np.repeat(label1, 100, axis = 0)

    samples3 = np.random.multivariate_normal([-5+x_bias, 5], [[1, 0],[0, 1]], 50)
    samples4 = np.random.multivariate_normal([5+x_bias, -5], [[1, 0],[0, 1]], 50)
    labels2 = np.repeat(label2, 100, axis = 0)
    
    samples = np.concatenate((samples1, samples2, samples3, samples4 ), axis =0)
    labels = np.concatenate((labels1, labels2 ), axis =0)
    # Plot the data
    plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
    plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
    plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
    plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
    plt.show()

# Split training and testing set

randomOrder = np.random.permutation(200)
#训练集与测试集
trainingX = samples[randomOrder[0:100], :]
trainingY = labels[randomOrder[0:100], :]
testingX = samples[randomOrder[100:200], :]
testingY = labels[randomOrder[100:200], :]
#创建神经元
model = Sequential()
#第一层
model.add(Dense(4, input_shape=(2,), activation='relu'))
#第二层
model.add(Dense(2, activation='softmax' ))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['binary_accuracy'])
#训练500次~
model.fit(trainingX, trainingY, epochs=500, batch_size=10, verbose=1, validation_split=0.2)

# score = model.evaluate(testingX, testingY, verbose=0)
score = 0
for i in range(100):
    estimate = model.predict_classes(np.array([testingX[i,:]]))

    if testingY[i,estimate] == 1:
        score = score  + 1

print('Test accuracy:', score/100)