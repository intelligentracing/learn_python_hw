import numpy as np 

def swap_rows(M, a, b):
    #saint check
    if type(M) is not np.ndarray:
        raise TypeError('M should be matrix type！')
    M_1 = M.copy()
    M_1[a-1] = M[b-1]
    M_1[b-1] = M[a-1]    
    
    return M_1

m = np.array([[[1,2,3],[3,4,5],[5,6,7]],[[11,2,3],[3,14,5],[5,61,7]],[[1,2,13],[3,4,25],[5,6,27]]])
print(swap_rows(m,2,3))

def swap_cols(M, a, b):
    #saint check
    if type(M) is not np.ndarray:
        raise TypeError('M should be matrix type！')
    M_1 = M.T.copy()
    M = M.T
    M_1[a-1] = M[b-1]
    M_1[b-1] = M[a-1]  
    M_1 = M_1.T  
    
    return M_1

m = np.array([[1,2,3],[3,4,5],[5,6,7]])
print(swap_cols(m,2,3))