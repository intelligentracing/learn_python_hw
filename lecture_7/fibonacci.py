## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: fibonacci.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

def fibonacci(n):
    ''' A recursive function to calculate the Fibonacci number
    Parameters:
    - Input: n an integer >= 0
    - Output: Integer Fibonacci number
    '''

    if type(n)!= int:
        raise TypeError('Incorrect Fibonacci argument type.')
    elif n<0:
        raise ValueError('Fibonacci argument must be greater than zero.')

    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(19))

print(fibonacci(-2))