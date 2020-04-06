import numpy as np
import matplotlib.pyplot as plt
import time

def hour_to_degree(hour,minute):
    return -(360/12*hour+360/12/60*minute)

def minute_to_degree(minute):
    return -360/60*minute

def rotationMatrix(degree):
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

def face():
    line=np.array([0.,5.])
    for i in range (12):
        l=rotationMatrix(hour_to_degree(i,0)).dot(line)
        plt.arrow(0,0,l[0],l[1],head_width=0, head_length=0, color = 'black')
        
face()
# print("Input hour of time please.")
# h=int(input())
# print("Input minute of time please.")
# m=int(input())
h=int(time.strftime("%H", time.localtime()))
m=int(time.strftime("%S", time.localtime()))
phour=np.array([0.,1.])
pminute=np.array([0.,3.])
hour=rotationMatrix(hour_to_degree(h,m)).dot(phour)
minute=rotationMatrix(minute_to_degree(m)).dot(pminute)
plt.arrow(0,0,hour[0],hour[1], head_width=0.3, head_length=0.5, color = 'b')
plt.arrow(0,0,minute[0],minute[1],head_width=0.3, head_length=0.5, color = 'r')
plt.axis([-7,7,-7,7])
plt.show()