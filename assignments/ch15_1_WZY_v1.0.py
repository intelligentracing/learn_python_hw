import numpy as np
import matplotlib.pyplot as plt
import datetime

def hour_to_degree(hour):
    return -360/12*hour

def minute_to_degree(minute):
    return -360/60*minute

def rotationMatrix(degree):
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

def face():
    line=np.array([0.,5.])
    for i in range (12):
        l=rotationMatrix(hour_to_degree(i)).dot(line)
        plt.arrow(0,0,l[0],l[1],head_width=0, head_length=0, color = 'black')
        
face()
print("Input hour of time please.")
h=int(input())
print("Input minute of time please.")
m=int(input())
phour=np.array([0.,1.])
pminute=np.array([0.,3.])
hour=rotationMatrix(hour_to_degree(h)).dot(phour)
minute=rotationMatrix(minute_to_degree(m)).dot(pminute)
plt.arrow(0,0,hour[0],hour[1], head_width=0.3, head_length=0.5, color = 'b')
plt.arrow(0,0,minute[0],minute[1],head_width=0.3, head_length=0.5, color = 'r')
plt.axis([-7,7,-7,7])
plt.show()