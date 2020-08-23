import os
import numpy as np 

path = os.path.dirname(os.path.abspath(__file__))
source_filename = 'AAPL_M4.csv'
source_handle = open(path+'/'+source_filename,'r')

prcie_dictionary = dict()
for line in source_handle.readlines()[1:]:
    line_list = line.split(',')
    prcie_dictionary[line_list[6]] = line_list[0]
#print(prcie_dictionary)
 
y_sample = np.zeros(365)
A_sample = np.zeros((365, 2))

key_list = []
for key in prcie_dictionary:
    for j in range(365):
        key_list.append(key) 
        A_sample[j] = [j,1]
for i in range(len(key_list)-365, len(key_list)):
    for k in range(365):
        y_sample[k] = key_list[i]
aa = np.linalg.lstsq(A_sample, y_sample, rcond = None)[0]
print(aa)

def price_estimate(x):
    return aa[0]*x + aa[1]

print(price_estimate(395))