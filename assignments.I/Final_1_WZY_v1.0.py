# DETERMINE IF A MATRIX IS FULL-RANK
# The rank of a square matrix determines if the matrix exists its inverse 
# and hence if a linear system that it represents can have a unique solution. 
# Whether the rank of a matrix is full can be tested by answering the following
# question: Whether there exists a non-zero vector x, such that Ax = 0.
# Please verify if the following two matrices are full rank, and if not 
# give an example of a nonzero vector that achieves the above condition:
# (1) A = [[−1, 3] [3, −9]]
# (2)A= [[sinθ, cosθ, 0 ]
# [cosθ, −sinθ, 0] 
# [0,0,1]]

import numpy as np
import matplotlib.pyplot as plt
import math
import random
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
θ = random.random()
A = np.array([[-1, 3], [3, -9]])
rightA=np.array([[-1, 3], [3, 9]])
B = np.array([[math.sin(θ), math.cos(θ), 0 ],[math.cos(θ), -math.sin(θ), 0] ,[0,0,1]])
print(np.linalg.matrix_rank(A)==2)
print(np.linalg.matrix_rank(rightA)==2)
print(np.linalg.matrix_rank(B)==3)