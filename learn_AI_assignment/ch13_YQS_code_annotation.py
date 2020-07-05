##test_VGG_pretrained.py
import keras
from keras.datasets import cifar100
import matplotlib.pyplot as plt
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import numpy as np
import cv2

# Load the pretrained VGG16 model and parameters
model = VGG16(weights='imagenet')
# Load CIFAR100
(x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode = 'fine')

# Test the x_test images without training
plt.figure(1)
for i in range(len(y_test)):
    test_image = x_test[i]
    #VGGmodel中的假设输入图像大小为224*224*3，
    # 所以cifar数据集中的图片要进行变形
    test_image = cv2.resize(test_image, (224, 224))
    display_image = test_image.copy()

    # Convert a single image into batch Keras training format
    test_image = test_image.reshape((1, 224, 224, 3))
    test_image = test_image.astype('float32')
    #preprocess_input完成数据预处理的工作包括归一化
    test_image = preprocess_input(test_image)

    # Predict and extract the top 3 text labels
    y_predict = model.predict(test_image)
    #decode_predictions输出top3的预测类别
    label = decode_predictions(y_predict)
    display_labels = str([label[0][0][1], label[0][1][1], label[0][2][1]])

    # Display the test result
    plt.imshow(display_image, cmap = plt.cm.binary)
    plt.title(display_labels)
    print(label)
    plt.show()

##CIFAR100_VGG_fixed_features.py
import keras
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.applications.vgg16 import VGG16
import numpy as np
import cv2

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
#include_top=False表示不带全连接网络
baseModel = VGG16(weights='imagenet', include_top=False, input_tensor=keras.Input(shape=input_shape))
for layer in baseModel.layers:
    #在fit时，如果trainable= False, 就不会不会更新网络权重参数
    layer.trainable = False

headModel = baseModel.output
headModel = Flatten(name='flatten')(headModel)
headModel = Dense(4096, activation = 'relu')(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(4096, activation = 'relu')(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(num_classes, activation = 'softmax')(headModel)

model = keras.Model(inputs=baseModel.input, outputs = headModel)
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.2)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])