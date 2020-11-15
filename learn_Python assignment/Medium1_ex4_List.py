#Midium1 ex4_List.py
#Author: Yu Qiuhsuang
from queue import deque
#input interface
element = input('please input the number for the list(eg:12345,without any sign between the numbers):')
shift = input('please input shift steps:')
shift = int(shift)
test_list = list(element)

#result_list is use to save the result that covert from the type of element in test_list 
result_list = []
for i in test_list:
    result_list.append(int(i))

# len()use to get the length of the input list
n = len(result_list)

# avoid repeat 
shift = shift % n

#result_list_copy is use to save the shifted results
result_list_copy = result_list.copy()
for s in range(n):
    if s + shift < n:
        result_list_copy[s + shift] = result_list[s]
    if s + shift >= n:
        result_list_copy[s + shift - n] = result_list[s]
print(result_list_copy)