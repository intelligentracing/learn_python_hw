from collections import deque
def recursive_function(user_deque, reverse = True):
    if user_deque == 1:
        return 1 
    else: 
        return  user_deque + recursive_function(user_deque-1)