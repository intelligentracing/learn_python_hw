import numpy as np
import random

A = np.array([[-1,3],[3,-9]])
theta = random.randint(0,360) * 2 * np.pi / 360
B = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
n = A.shape[0]
m = B.shape[0]
if np.linalg.matrix_rank(A) < n:
    a1 = random.randint(1,10)
    b1 = 3 * a1
    print(np.linalg.matrix_rank(A),'<',n,'矩阵A不满秩，x的任意一个非零向量解为：',[a1, b1])

else:
    print('the rank of A is full.')
if np.linalg.matrix_rank(B) < m:
    b1 = random.randint(1,10)
    b2 = np.cos(theta) / np.sin(theta) * b1
    print(np.linalg.matrix_rank(B),'<',m,'矩阵A不满秩，x的任意一个非零向量解为：',[b1, b2])
else:
    print('the rank of B is full.')