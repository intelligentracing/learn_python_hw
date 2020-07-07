## This is course material for Introduction to Modern Artificial Intelligence
## Class 14 Example code: train_VGG_fixed_features_augmentation.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, MaxPool2D
from keras.applications.vgg16 import VGG16
import numpy as np
import cv2
from keras.preprocessing.image import ImageDataGenerator

batch_size = 100
num_classes = 100
epochs = 100

# input image dimensions
img_rows, img_cols, img_depth = 112, 112, 3

# load the data built in Keras, split between train and test sets
(CIFAR_x_train, y_train), (CIFAR_x_test, y_test) = cifar100.load_data(label_mode = 'fine')

# resize input images to VGG16 input size
train_n = len(y_train)
x_train = np.zeros((train_n, img_rows, img_cols, img_depth), dtype = 'uint8')
for i in range(train_n):
    temp_image = CIFAR_x_train[i]
    temp_image = cv2.resize(temp_image, (img_rows, img_cols))
    x_train[i,:,:,:] = temp_image

test_n = len(y_test)
x_test = np.zeros((test_n, img_rows, img_cols, img_depth), dtype = 'uint8')
for i in range(test_n):
    temp_image = CIFAR_x_test[i]
    temp_image = cv2.resize(temp_image, (img_rows, img_cols))
    x_test[i,:,:,:] = temp_image

input_shape = (img_rows, img_cols, img_depth)

# When calculating image data, convert from uint8 to float
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255
print('x_train shape:', x_train.shape)

# Image Augmentation
train_datagen = ImageDataGenerator(
        samplewise_center = True,
        width_shift_range=0.1, height_shift_range=0.1, shear_range = 30,
        fill_mode='nearest',
        horizontal_flip=True)
standardization_flag = False

# When ImageDataGenerator includes featurewise_center or zca, needs a fit data
if standardization_flag:
    # Collect data statistics
    train_datagen.fit(x_train)

# Apply preprocessing to the test images
for i in range(len(y_test)):
    x_test[i] = train_datagen.standardize(x_test[i])

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

baseModel = VGG16(weights='imagenet', include_top=False, input_tensor=keras.Input(shape=input_shape))
for layer in baseModel.layers:
    layer.trainable = False

headModel = baseModel.output
headModel = MaxPool2D(pool_size=(2,2))(headModel)
headModel = Flatten(name='flatten')(headModel)
headModel = Dense(1024, activation = 'relu')(headModel)
headModel = Dropout(0.75)(headModel)
headModel = Dense(1024, activation = 'relu')(headModel)
headModel = Dropout(0.75)(headModel)
headModel = Dense(num_classes, activation = 'softmax')(headModel)

model = keras.Model(inputs=baseModel.input, outputs = headModel)
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(lr=0.0001),
              metrics=['accuracy'])

#model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.2)
model.fit_generator(train_datagen.flow(x_train, y_train, batch_size = batch_size),
 validation_data=(x_test, y_test), verbose=1, epochs = epochs)

score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])