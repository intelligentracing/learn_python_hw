###1.Linear Algebra###
import numpy as np
import math
'''这是一个证明A = ([-1,3],[3,-9])与AA = ([cos(s),-sin(s),0],[sin(s),cos(s),cos(s),0],[0,0,1])是否满秩的方法。
   '''

def IfFullRank(a):##求是否满秩
    Ainv = np.linalg.inv(a)
    x = Ainv.dot(0)
    if x = 0:
        print(a,"is full rank.")
    else:
        print(x)
        print(a,'is not full rank.')
s = random.randint(0,360) * 2 * np.pi / 360        
A = ([-1,3],[3,-9])
AA = ([math.cos(s),-math.sin(s),0],[math.sin(s),math.cos(s),math.cos(s),0],[0,0,1])
IfFullRank(A)
IfFullRank(AA)

