import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os


path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
GMT_hand_length = 50
GMT_hand_width = 4
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

while True:
    plt.imshow(background)
    plt.axis('off')#Horizontal and vertical coordinates are not displayed
    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour + now_time.minute / 60 + now_time.second /3600 #把当前的分钟和秒钟也变换为小时，换算成时针需要转的角度
    GMT_time = hour - 8
    if hour>12: hour = hour - 12
    minute = now_time.minute + now_time.second / 60 #把当前的秒钟也变换为分钟，换算成分针需要转的角度
    second = now_time.second

    # Calculate end points of hour, minute, second

    hour_vector = clock_hand_vector(hour/12*2*np.pi, hour_hand_length)
    minute_vector = clock_hand_vector(minute/60*2*np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)
    GMT_vector = clock_hand_vector(GMT_time/24 *2*np.pi, GMT_hand_length)

    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'green')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')
    plt.arrow(center[0], center[1],GMT_vector[0], GMT_vector[1], linewidth = GMT_hand_width, color = 'yellow')
    plt.pause(0.1)#根据pyplot绘制图像，每隔0.1s执行一遍
    plt.clf() # Clear figure清除所有轴，但是窗口打开，这样它可以被重复使用
