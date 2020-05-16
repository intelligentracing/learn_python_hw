from collections import deque

def recursive_function(input_deque):

    if type(input_deque) != deque :
        raise TypeError('Input arguments are not allowed.')

    if len(input_deque) == 1:
        result = input_deque.pop()
        print(result) 
        return
    input_deque.pop()
    recursive_function(input_deque)


input_deque = deque([1,2,3,4,5])
recursive_function(input_deque)
print (input_deque)