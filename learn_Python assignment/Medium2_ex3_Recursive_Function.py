#Midium2 ex3_Recursive_Function.py
#Author: Yu Qiuhsuang

from collections import deque

def dequeue(input_deque, reverse = False):

    if type(input_deque) != deque or type(reverse) != bool:
        raise TypeError('Input arguments are not allowed.')
    
    middle_queue = deque()
    if len(input_deque) == 1:
        result = input_deque.pop()
        return result

    middle_queue.append(input_deque.pop())
    dequeue(input_deque)


input_deque = deque([1,2,3,4,5])
print(dequeue(input_deque))