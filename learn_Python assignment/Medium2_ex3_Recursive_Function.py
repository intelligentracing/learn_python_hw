#Midium2 ex3_Recursive_Function.py
#Author: Yu Qiuhsuang

from collections import deque

def recursive_function(input_deque, reverse = False):

    if type(input_deque) != deque or type(reverse) != bool:
        raise TypeError('Input arguments are not allowed.')

    if len(input_deque) == 1:
        result = input_deque.pop()
        print(result) 
        return
    input_deque.pop()
    recursive_function(input_deque)


input_deque = deque([1,2,3,4,5])
recursive_function(input_deque)