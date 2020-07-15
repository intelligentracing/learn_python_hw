import keras
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
import cv2
import os

model = ResNet50(weights='imagenet')

window_size = 224
sliding_window_step = 8
detection_threshold = 0.9

# load the test image: three_horses.jpg
path = os.path.dirname(os.path.abspath(__file__))
image = cv2.imread(path + '/zebras.jpg')


# First, test classify the full image
# resized_image = cv2.resize(image,(224,224))
# resized_image = resized_image.reshape((1, window_size, window_size, 3))
# resized_image = preprocess_input(resized_image)
# y_predict = model.predict(resized_image)
# label = decode_predictions(y_predict)
# print(label)
# classifier哪种网络结构，debug表示是否用debug来运行该函数
def nms(x1, y1, x2, y2, scores, thresh):
    # initialize the list of picked indexes
    # x1、y1、x2、y2、以及score赋值
    x1 = np.array(x1)
    y1 = np.array(y1)
    x2 = np.array(x2)
    y2 = np.array(y2)
    scores = np.array(scores)
    # 每一个候选框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = scores.argsort()
    # order是按照score降序排序的
    # order = scores.argsort()[::-1]

    pick = []
    while len(idxs) > 0:
        # grab the last index in the indexes list, add the index
        # value to the list of picked indexes, then initialize
        # the suppression list (i.e. indexes that will be deleted)
        # using the last index
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        suppress = [last]
        for pos in range(0, last):
            # grab the current index
            j = idxs[pos]
            # find the largest (x, y) coordinates for the start of
            # the bounding box and the smallest (x, y) coordinates
            # for the end of the bounding box
            xx1 = max(x1[i], x1[j])
            yy1 = max(y1[i], y1[j])
            xx2 = min(x2[i], x2[j])
            yy2 = min(y2[i], y2[j])
            # compute the width and height of the bounding box
            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)
            # compute the ratio of overlap between the computed
            # bounding box and the bounding box in the area list
            overlap = float(w * h) / areas[i]
            # if there is sufficient overlap, suppress the
            # current bounding box
            if overlap > thresh:
                suppress.append(pos)
        # delete all indexes from the index list that are in the
        # suppression list
        idxs = np.delete(idxs, suppress)
    # return only the bounding boxes that were picked
    return x1[pick], y1[pick]


def sliding_window_detector(image, window_size, step, classifier, object_string, debug=False):
    image_H, image_W, image_D = image.shape
    return_probability = np.zeros((image_H, image_W))
    # 要进行debug操作，应该对copy出来的数据进行debug，所以都要先用copy()把原图copy出来
    if debug:
        debug_image = image.copy()

    print('Detecting {0}x{1}'.format(image_H, image_W))
    for h in range(0, image_H - window_size, step):
        for w in range(0, image_W - window_size, step):
            # image_window是224*224的滑动窗口大小，我们对这么大的滑动窗口进行图像识别判断其label,得到的是一个窗口的label
            image_window = image[h:h + window_size, w:w + window_size, :]
            image_window = image_window.reshape((1, window_size, window_size, 3))
            image_window = preprocess_input(image_window)
            y_predict = model.predict(image_window)
            label = decode_predictions(y_predict)
            for label_index in range(5):
                if label[0][label_index][1] == object_string and label[0][label_index][2] > detection_threshold:
                    # 高于置信度的放到return_probability
                    return_probability[h, w] = label[0][label_index][2]
                    print('*', end='')

                    # if debug:
                    #     top_left_corner = (w, h)
                    #     bottom_right_corner = (w+window_size, h+window_size)
                    # debug_image = cv2.rectangle(debug_image, top_left_corner, bottom_right_corner, (0,0,255), 4)
                    # cv2.imshow('Sliding Window', debug_image)
                    # cv2.waitKey(10)

    if debug:
        debug_image = image.copy()
        x1 = []
        y1 = []
        score = []
        for i in range(image_H):
            for j in range(image_W):
                if return_probability[i, j] != 0:
                    x1.append(i)
                    y1.append(j)
        score.append(return_probability[i, j])
        x2 = [h + window_size for h in x1]
        y2 = [w + window_size for w in y1]

        x_box, y_box = nms(x1, y1, x2, y2, score, 0.5)  # 0.3为faster-rcnn中配置文件的默认值
        for h, w in zip(x_box, y_box):
            top_left_corner = (w, h)
            bottom_right_corner = (w + window_size, h + window_size)
            debug_image = cv2.rectangle(debug_image, top_left_corner, bottom_right_corner, (0, 0, 255), 4)
        cv2.imshow('Sliding Window', debug_image)
        cv2.waitKey(10)

    print('Done!')
    return return_probability


downsample_stages = 3
return_labels = []
image_H, image_W, image_D = image.shape
image = cv2.resize(image, (int(image_W / 1.5), int(image_H / 1.5)))
# 对图像下采样
for downsample in range(downsample_stages):
    image_H, image_W, image_D = image.shape
    image_H = int(image_H / 1.5);
    image_W = int(image_W / 1.5)
    image = cv2.resize(image, (image_W, image_H))
    detection = sliding_window_detector(image, window_size, sliding_window_step, model, 'zebra', True)
    cv2.waitKey(0)