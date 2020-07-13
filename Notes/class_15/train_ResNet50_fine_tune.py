## This is course material for Introduction to Modern Artificial Intelligence
## Class 15 Example code: train_ResNet50_fine_tune.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from keras.applications.resnet50 import ResNet50, preprocess_input
import numpy as np
import cv2
from keras.preprocessing.image import ImageDataGenerator

batch_size = 100
num_classes = 100
epochs = 100

<<<<<<< HEAD
# input image dimensions
img_rows, img_cols, img_depth = 112, 112, 3

# load the data built in Keras, split between train and test sets
(CIFAR_x_train, y_train), (CIFAR_x_test, y_test) = cifar100.load_data(label_mode = 'fine')

# resize input images to VGG16 input size
train_n = len(y_train)
x_train = np.zeros((train_n, img_rows, img_cols, img_depth), dtype = 'uint8')
=======
#确定图像维度(参数)
img_rows, img_cols, img_depth = 112, 112, 3

#加载数据,分离测试组和训练组
(CIFAR_x_train, y_train), (CIFAR_x_test, y_test) = cifar100.load_data(label_mode = 'fine')

#修改图像大小
train_n = len(y_train)
x_train = np.zeros((train_n, img_rows, img_cols, img_depth), dtype = 'uint8')
#遍历所有图像,训练
>>>>>>> db611735913dd117a197baa4d2b29d3be9095ef1
for i in range(train_n):
    temp_image = CIFAR_x_train[i]
    temp_image = cv2.resize(temp_image, (img_rows, img_cols))
    temp_image = preprocess_input(temp_image)
    x_train[i,:,:,:] = temp_image
<<<<<<< HEAD

=======
#遍历所有图像,测试
>>>>>>> db611735913dd117a197baa4d2b29d3be9095ef1
test_n = len(y_test)
x_test = np.zeros((test_n, img_rows, img_cols, img_depth), dtype = 'uint8')
for i in range(test_n):
    temp_image = CIFAR_x_test[i]
    temp_image = cv2.resize(temp_image, (img_rows, img_cols))
    temp_image = preprocess_input(temp_image)
    x_test[i,:,:,:] = temp_image

input_shape = (img_rows, img_cols, img_depth)

<<<<<<< HEAD
# When calculating image data, convert from uint8 to float
=======
#修改图像格式
>>>>>>> db611735913dd117a197baa4d2b29d3be9095ef1
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

# Reduce the element range from [0, 255] to [0, 1]
print('x_train shape:', x_train.shape)

<<<<<<< HEAD
# Image Augmentation
=======
#生成垃圾图像(自动增加训练集)
>>>>>>> db611735913dd117a197baa4d2b29d3be9095ef1
train_datagen = ImageDataGenerator(
        width_shift_range=0.25, height_shift_range=0.25, shear_range = 30,
        rotation_range = 10,
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

<<<<<<< HEAD
# To retrain all layers
=======
#加载基础模型文件格式
>>>>>>> db611735913dd117a197baa4d2b29d3be9095ef1
baseModel = ResNet50(weights='imagenet', include_top=False, pooling = 'avg', input_tensor=keras.Input(shape=input_shape))

headModel = baseModel.output
headModel = Dense(num_classes, activation = 'softmax')(headModel)

model = keras.Model(inputs=baseModel.input, outputs = headModel)

<<<<<<< HEAD
# To train model with decreasing learning rates
sdg = keras.optimizers.SGD(lr = 0.01,#学习速率
                            decay = 1e-3, #学习效率消减因子
                            momentum = 0.5, #
=======
#训练
#Stochastic gradiant decent
sdg = keras.optimizers.SGD(lr = 0.01, #学习速率
                            decay = 1e-3, #学习效率消减因子
                            momentum = 0.5,  #波动值(防止收敛到局部最优解)
>>>>>>> db611735913dd117a197baa4d2b29d3be9095ef1
                            nesterov = True)
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=sdg,
              metrics=['accuracy'])
    
model.fit_generator(train_datagen.flow(x_train, y_train, batch_size = batch_size),
    validation_data=(x_test, y_test), verbose=1, epochs = epochs)

score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])