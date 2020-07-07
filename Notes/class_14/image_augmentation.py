## This is course material for Introduction to Modern Artificial Intelligence
## Class 14 Example code: image_augmentation.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#加载数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# reshape to be [samples][width][height][channels]
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

## convert from int to float
#X_train = X_train.astype('float32')
#X_test = X_test.astype('float32')

#在0~90旋转
datagen = ImageDataGenerator(rotation_range=90)
# fit parameters from data
datagen.fit(X_train)

#一次9个训练
for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9):
	# create a grid of 3x3 images
	for i in range(0, 9):
		pyplot.subplot(330 + 1 + i)
		pyplot.imshow(X_batch[i].reshape(28, 28), cmap=pyplot.get_cmap('gray'))
	# show the plot
	pyplot.show()
	break

#图像位移
datagen = ImageDataGenerator(width_shift_range = 0.25, height_shift_range = 0.25)
# fit parameters from data
datagen.fit(X_train)

#展示图像
for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9):
	# create a grid of 3x3 images
	for i in range(0, 9):
		pyplot.subplot(330 + 1 + i)
		pyplot.imshow(X_batch[i].reshape(28, 28), cmap=pyplot.get_cmap('gray'))
	# show the plot
	pyplot.show()
	break

#水平翻转
datagen = ImageDataGenerator(horizontal_flip=True)
# fit parameters from data
datagen.fit(X_train)

#展示图像
for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9):
	# create a grid of 3x3 images
	for i in range(0, 9):
		pyplot.subplot(330 + 1 + i)
		pyplot.imshow(X_batch[i].reshape(28,28), cmap=pyplot.get_cmap('gray'))
	# show the plot
	pyplot.show()
	break

#压缩,延展图像
datagen = ImageDataGenerator(shear_range=60)
# fit parameters from data
datagen.fit(X_train)

#展示图像
for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9):
	# create a grid of 3x3 images
	for i in range(0, 9):
		pyplot.subplot(330 + 1 + i)
		pyplot.imshow(X_batch[i].reshape(28,28), cmap=pyplot.get_cmap('gray'))
	# show the plot
	pyplot.show()
	break

#信号白化,使数据均匀正态分布
datagen = ImageDataGenerator(zca_whitening = True)
# fit parameters from data
datagen.fit(X_train)

#展示图像
for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9):
	# create a grid of 3x3 images
	for i in range(0, 9):
		pyplot.subplot(330 + 1 + i)
		pyplot.imshow(X_batch[i].reshape(28,28), cmap=pyplot.get_cmap('gray'))
	# show the plot
	pyplot.show()
	break