## This is course material for Introduction to Modern Artificial Intelligence
## Class 14 Example code: train_VGG_fine_tune.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, MaxPool2D
from keras.applications.vgg16 import VGG16
import numpy as np
import tensorflow as tf
import cv2
import glob
import os
from keras.preprocessing.image import ImageDataGenerator

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
x_test = []
for filename in glob.glob(r'C:\Users\mac\Documents\GitHub\learn_python_hw\learn_AI_assignment\CH13_picture\*'):
    test_image = cv2.imread(filename)
    x_test.append(test_image)
# Load the pretrained VGG16 model and parameters
model = VGG16(weights='cp_calback')

# Test the x_test images without training
plt.figure(1)
for i in range(len(x_test)):
    test_image = cv2.resize(x_test[i], (224, 224))
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

