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
# (2) For every point at coordinates [x, y], evaluate its probability with 
# respect to Model 0 and Model 1, and perform the classification.
# (3) In a 2D pyplot figure, plot all the above points and associate their 
# classification using different marker colors: red for Model 0 and blue 
# for Model 1.
# (4) From this experiment, answer: What is the decision boundary of two 
# Gaussian models in 2D.
import numpy as np
import matplotlib.pyplot as plt
import random

mu0 = [1, 2]
sigma0 = 1
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
        print([round(x,1),round(y,1)],'belonging to Model_0.')
        x_sample_0.append(round(x,1))
        y_sample_0.append(round(y,1))
        plt.plot(x_sample_0,y_sample_0,'r.')
    else:
        print([round(x,1), round(y,1)], 'belonging to Model_1.')
        x_sample_1.append(round(x, 1))
        y_sample_1.append(round(y, 1))
        plt.plot(x_sample_1, y_sample_1, 'c.')

x_rr,y_rr = np.meshgrid(np.arange(-5,5,0.1),np.arange(-5,5,0.1))


for i in range(len(x_rr[0])):
    x=(random.randint(0,100)/10)-5
    y=(random.randint(0,100)/10)-5
    proability(x,y)

plt.show()

