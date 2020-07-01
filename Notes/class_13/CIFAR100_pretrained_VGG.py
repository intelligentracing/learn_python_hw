## This is course material for Introduction to Modern Artificial Intelligence
## Class 13 Example code: CIFAR100_cnn.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import keras
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras import backend as K
import matplotlib.pyplot as plt
from keras.applications.vgg16 import VGG16

training_size = 40000
batch_size = training_size//100
num_classes = 100
epochs = 100

# input image dimensions
img_rows, img_cols, img_depth = 32, 32, 3

# load the data built in Keras, split between train and test sets
(x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode = 'fine')

# Display some examples from first 20 images
print(y_train[0:20])
plt.figure(1)
for i in range(20):
    plt.subplot(2,10,i+1)
    plt.imshow(x_train[i], cmap = plt.cm.binary)
plt.show()

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, img_depth)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, img_depth)
input_shape = (img_rows, img_cols, img_depth)

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

baseModel = VGG16(weights='imagenet', include_top=False, input_tensor=keras.Input(shape=(32,32,3)))
for layer in baseModel.layers:
    layer.trainable = False

headModel = baseModel.output
#headModel = AveragePooling2D(pool_size=(4,4))(headModel)
headModel = Flatten(name='flatten')(headModel)
headModel = Dense(128, activation = 'relu')(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(num_classes, activation = 'softmax')(headModel)

model = keras.Model(inputs=baseModel.input, outputs = headModel)

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.adam(lr=0.001),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_split=0.2)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])