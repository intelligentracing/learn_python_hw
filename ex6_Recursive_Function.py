from collections import deque

def recursive_function(input_deque, reverse = False):

    if type(input_deque) != deque or type(reverse) != bool:
        raise TypeError('Input arguments are not allowed.')

    if len(input_deque) == 1:
        return input_deque

    medile_list = []
    for i in range(len(input_deque)):
        letter = input_deque.pop()
        medile_list.append(letter)

    return  medile_list.pop()

input_deque = deque([2,3,4,5])
print(recursive_function(input_deque))