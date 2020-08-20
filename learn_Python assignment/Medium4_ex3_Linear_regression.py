import os
import numpy as np 

path = os.path.dirname(os.path.abspath(__file__))
source_filename = 'AAPL_M4.csv'
source_handle = open(path+'/'+source_filename,'r')

prcie_dictionary = dict()
for line in source_handle.readlines()[1:]:
    line_list = line.split(',')
    prcie_dictionary[line_list[6]] = line_list[0]
print(prcie_dictionary)