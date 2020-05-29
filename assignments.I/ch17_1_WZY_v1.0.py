import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

x, y = np.meshgrid(range(-5, 5), range(-5, 5))

z1 = 1-x
z2 = 2-x-y
z3 = 1-x+y

ax3d = plt.axes(projection = '3d')
ax3d.plot_surface(x, y, z1, color = 'red', alpha = 0.5 )
ax3d.plot_surface(x, y, z2, color = 'green', alpha = 0.5 )
ax3d.plot_surface(x, y, z3, color = 'blue', alpha = 0.5 )

ax3d.scatter(1, -2, -2, 'ko')
plt.show()