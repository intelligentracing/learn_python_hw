# CLASSIFICATION BASED ON MIXED GAUSSIAN MODELS
# Assume there exist two 2-D Gaussian models in 2-D space. The first model is
# parametrized by a 2-D mean μ0 = [1,2] and a single standard deviation
# σX = σY = σ0 = 1. The second model by its mean μ1 = [−3,1] and a single
# standard deviation σX = σY = σ1 = 1.5. Based on the following probability
# function to calculate circular Gaussian models:
# f([x,y])= 1 exp((x−μx)2+(y−μy)2), 2πσ2 2σ2
# calculate the classification of sample points that may belong to either 
# Model 0 or Model 1.
# (1) Use numpy.meshgrid() to generate a grid of samples between -5 and 5 
# for both X axis and Y axis and use stepsize = 0.1.
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])


ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


plt.show()
# (2) For every point at coordinates [x, y], evaluate its probability with 
# respect to Model 0 and Model 1, and perform the classification.

def func(μx,μy,σ):
    f [x,y]= (1/2*math.pi*σ)*math.exp(((x-μx)**2+(y-μy)**2)/2*σ**2)

x = np.arange(-5, 5, 0.1)
y = func(-5,5,0.1)

plt.plot(y, 'r-', linewidth = 3)

μ0 = [1,2] 
σ0=1
σ1=1.5
μ1 = [-3,1] 
# (3) In a 2D pyplot figure, plot all the above points and associate their 
# classification using different marker colors: red for Model 0 and blue 
# for Model 1.
# (4) From this experiment, answer: What is the decision boundary of two 
# Gaussian models in 2D.


