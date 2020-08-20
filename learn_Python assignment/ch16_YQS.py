import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

#ex1.1
# fig, ax = plt.subplots()
# ax.spines['left'].set_position(('data',0))#将横纵坐标对齐
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# #第一个正方形的横坐标数组
# x0 = np.array([4,7,7,4,4])
# y0 = np.array([0,0,3,3,0])
# plt.plot(x0, y0, color = 'r', linewidth = 2)

# #第二个正方形的横坐标数组
# x1 = np.array([7,7,11,11,7])
# y1 = np.array([3,7,7,3,3])
# plt.plot(x1, y1, 'b', linewidth = 1)

# #第三个正方形的横坐标数组
# x2 = np.array([4,7,3,0,4])
# y2 = np.array([3,7,10,6,3])
# plt.plot(x2, y2, 'y', linewidth = 3)

# #使横纵坐标单位长度统一
# plt.axis('scaled')
# plt.xticks(np.arange(0,12,2))
# plt.yticks(np.arange(0,12,2))
# plt.show()
#ex1.2

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

while True:
    plt.imshow(background)
    plt.axis('off')#不显示横纵坐标
    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour + now_time.minute / 60 + now_time.second /3600#把当前的分钟和秒钟也变换为小时，换算成时针需要转的角度
    if hour>12: hour = hour - 12
    minute = now_time.minute + now_time.second / 60#把当前的秒钟也变换为分钟，换算成分针需要转的角度
    second = now_time.second

    # Calculate end points of hour, minute, second

    hour_vector = clock_hand_vector(hour/12*2*np.pi, hour_hand_length)
    minute_vector = clock_hand_vector(minute/60*2*np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)

    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')

    plt.pause(0.1)#根据pyplot绘制图像，每隔0.1s执行一遍
    plt.clf()
