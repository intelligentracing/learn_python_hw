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

# Create data
linearSeparableFlag = False
x_bias = 0
label1 = np.array([[1, 0]])
label2 = np.array([[0, 1]])
if linearSeparableFlag:

    samples1 = np.random.multivariate_normal([5 + x_bias, 0], [[1, 0], [0, 1]], 100)

    labels1 = np.repeat(label1, 100, axis=0)

    samples2 = np.random.multivariate_normal([-5 + x_bias, 0], [[1, 0], [0, 1]], 100)
    labels2 = np.repeat(label2, 100, axis=0)

    samples = np.concatenate((samples1, samples2), axis=0)
    labels = np.concatenate((labels1, labels2), axis=0)
    # Plot the data
    plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
    plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
    plt.show()

else:
    samples1 = np.random.multivariate_normal([5 + x_bias, 5], [[1, 0], [0, 1]], 50)
    samples2 = np.random.multivariate_normal([-5 + x_bias, -5], [[1, 0], [0, 1]], 50)
    labels1 = np.repeat(label1, 100, axis=0)

    samples3 = np.random.multivariate_normal([-5 + x_bias, 5], [[1, 0], [0, 1]], 50)
    samples4 = np.random.multivariate_normal([5 + x_bias, -5], [[1, 0], [0, 1]], 50)
    labels2 = np.repeat(label2, 100, axis=0)

    samples = np.concatenate((samples1, samples2, samples3, samples4), axis=0)
    labels = np.concatenate((labels1, labels2), axis=0)
    # Plot the data
    plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
    plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
    plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
    plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
    plt.show()

# Split training and testing set

randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[0:100], :]
trainingY = labels[randomOrder[0:100], :]
testingX = samples[randomOrder[100:200], :]
testingY = labels[randomOrder[100:200], :]

model = Sequential()
model.add(Dense(10, input_shape=(2,), activation='sigmoid'))
model.add(Dense(2, activation='softmax'))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['binary_accuracy'])

model.fit(trainingX, trainingY, epochs=1000, batch_size=20, verbose=1, validation_split=0.2)

# score = model.evaluate(testingX, testingY, verbose=0)
score = 0
for i in range(100):
    estimate = model.predict_classes(np.array([testingX[i, :]]))

    if testingY[i, estimate] == 1:
        score = score + 1

print('Test accuracy:', score / 100)

#(2+1)*10+(10+1)*2=55个
#总参数为55个