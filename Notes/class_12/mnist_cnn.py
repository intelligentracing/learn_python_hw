## This is course material for Introduction to Modern Artificial Intelligence
## Class 12 Example code: mnist_cnn.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import matplotlib.pyplot as plt
#防止报错
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#convolutional neural network CNN
batch_size = 128
num_classes = 10
epochs = 8

# input image dimensions
img_rows, img_cols = 28, 28

# load the data built in Keras, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Display some examples from first 20 images
print(y_train[0:20])
plt.figure(1)
for i in range(20):
    plt.subplot(2,10,i+1)
    plt.imshow(x_train[i], cmap = plt.cm.binary)
plt.show()

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

# When calculating image data, convert from uint8 to float
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Reduce the element range from [0, 255] to [0, 1]
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# CNN is created also using Sequential model
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5),#滤镜大小
                 strides=(1,1),#步长
                 padding="valid",#边界填充
                 activation='relu',#激发函数
                 input_shape=input_shape))

#在每一个矩阵中获取最大输出
model.add(MaxPooling2D(pool_size=(2, 2),#窗口大小
                        strides=None,#默认kxk步长(不重叠)
                        padding="valid"))#边界数据处理

#随机选举神经元进入休眠状态(防止过度训练,有利于算法收敛,仅用于训练)
model.add(Dropout(0.25))
model.add(Conv2D(64, kernel_size=(5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='Adadelta',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_split=0.2)
score = model.evaluate(x_test, y_test, verbose=0)
print(model.summary())
print('Test loss:', score[0])
print('Test accuracy:', score[1])

## Save the model
model.save('MNIST_CNN.h5')