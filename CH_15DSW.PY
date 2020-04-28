import numpy as np
import matplotlib.pyplot as plt

def rotationMatrix(degree):
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

v1 = np.array([1.,3.])
rotation_matrix = rotationMatrix(45)

v2 = rotation_matrix.dot(v1)

plt.arrow(0,0,v1[0],v1[1], head_width=0.8, head_length=0.8, color = 'b')
plt.arrow(0,0,v2[0],v2[1],head_width=0.8, head_length=0.8, color = 'r')
plt.axis([-5,5,0,10])
plt.show()