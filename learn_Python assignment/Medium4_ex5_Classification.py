import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from math import exp
from math import pi
from scipy.stats import multivariate_normal
# the first model
mu0 = [1, 2]
sigma0 = 1
#the second model
mu1 = [-3, 1]
sigma1 = 1.5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
x_sample_0 = []
y_sample_0 = []
x_sample_1 = []
y_sample_1 = []

def proability(x, y):
    proability0 = 1 / (2 * np.pi* sigma0)*np.exp(((x - mu0[0])**2 + (y - mu0[1])**2) / (2*sigma0**2))
    proability1 = 1 / (2 * np.pi * sigma1) * np.exp(((x - mu1[0]) ** 2 + (y - mu1[1]) ** 2) / (2 * sigma1 ** 2))
    if proability0 > proability1:
        x_sample_0.append(round(x,1))
        y_sample_0.append(round(y,1))
    plt.plot(x_sample_0,y_sample_0,'r*')

    if proability1 > proability0: 
        x_sample_1.append(round(x, 1))
        y_sample_1.append(round(y, 1))
    plt.plot(x_sample_1, y_sample_1, 'bD')
#(1) Use numpy.meshgrid() to generate a grid of samples between -5 and 5 for both X axis and Y axis and use stepsize = 0.1.
x_rr,y_rr = np.meshgrid(np.arange(-5,5,0.1),np.arange(-5,5,0.1))

for i in range(len(x_rr[0])):
    for j in range(len(y_rr[0])):
        proability(x_rr[i][j],y_rr[i][j])

plt.show()