## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: fibonacci.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

def fibonacci(i):
    ''' A recursive function to calculate the Fibonacci number
    Parameters:
    - Input: n an integer >= 0
    - Output: Integer Fibonacci number
    '''

    if type(i)!= int:
        raise TypeError('Incorrect Fibonacci argument type.')
    elif i<0:
        raise ValueError('Fibonacci argument must be greater than zero.')

    if i == 0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

print("Which one you need?")
i=int(input())
print(str(fibonacci(i)))
