import numpy as np

def Nearest_Neighbor(float_element, query_element):
    minimun = np.inf
    result = 0
    for i in range(len(float_element)):
        differences = abs(float_element[i] - query_element)
        if differences < minimun:
            minimun = differences
            result = float_element[i]
    return result

float_element = [1,2,3,4,5,6,7,8,9,10,50,20,30,40,60,70,80,90,500]
print(Nearest_Neighbor(float_element,452))