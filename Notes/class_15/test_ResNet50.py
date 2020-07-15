## This is course material for Introduction to Modern Artificial Intelligence
## Class 15 Example code: test_ResNet50.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

#在mac上运行AMDGPU:
# import os
#os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import keras
from keras.datasets import cifar100
import matplotlib.pyplot as plt
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
import cv2

model = ResNet50(weights='imagenet')
print(model.summary())

# load the data built in Keras, split between train and test sets
(x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode = 'fine')

# Test the x_test images without training
#加载数据
(x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode = 'fine')

plt.figure(1)
for i in range(len(y_test)):
    test_image = x_test[i]
    test_image = cv2.resize(test_image, (224, 224))
    display_image = test_image.copy()

    # Convert a single image into batch Keras training format
    test_image = test_image.reshape((1, 224, 224, 3))
    test_image = test_image.astype('float32')
    test_image = preprocess_input(test_image)

    # Predict and extract the top 3 text labels
    y_predict = model.predict(test_image)
    label = decode_predictions(y_predict)
    display_labels = str([label[0][0][1], label[0][1][1], label[0][2][1]])

    # Display the test result
    plt.imshow(display_image, cmap = plt.cm.binary)
    plt.title(display_labels)
    print(label)
    plt.show()