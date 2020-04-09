from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

z_line = np.linspace(0, 100, 1000)
x_line = np.linspace(0, 100, 1000)
y_line = np.linspace(0, 100, 1000)
ax.plot3D(x_line, y_line, z_line, 'white')

z_points = 100* np.random.random(100)
x_points = 100 * np.random.random(100)
y_points = 100 * np.random.random(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv')

plt.show()