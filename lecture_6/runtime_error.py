## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: runtime_error.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Most popular runtime error examples

import time

EXAMPLE_TO_RUN = 8

if EXAMPLE_TO_RUN == 0:
    # ********  Case 1: Using rserved words  ********
    int = 123
    float = int(10.57)
elif EXAMPLE_TO_RUN == 1:
    # ********  Case 2:  Forget to cast variable ********
    try:
        result = 'abcde' + 5
    except TypeError:
        print('TypeError occurred!')

elif EXAMPLE_TO_RUN == 2:
    # ********  Case 7:  Access a list element that doesn't exist ********
    animal_list = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
    try:
        print(animal_list[7])
    except IndexError:
        print('IndexError occurred!')
elif EXAMPLE_TO_RUN == 3:
    x = 0; y=0
    try:
        result = x/y
    except ZeroDivisionError:
        print('ZeroDivisionError occurred!')
elif EXAMPLE_TO_RUN == 4:
    try:
        import Math
    except ModuleError:
        print('ModuleError occurred!')       
elif EXAMPLE_TO_RUN == 5:
    try:
        result = int('year2020')
    except ValueError:
        print('ValueError occurred!')    
elif EXAMPLE_TO_RUN == 6:
    try:
        print(animal_list)
    except NameError:
        print('NameError occurred!')
elif EXAMPLE_TO_RUN == 7:
    try:
        result = input("Please input a string:")
    except KeyboardInterrupt:
        print("\n keyboardInterrupt occurred!")
elif EXAMPLE_TO_RUN == 8:
    try:
        f = open('myfile.txt')
    except OSError as error_message:
        print("OS Error: No.{0}. Message: {1}".format(\
            error_message.args[0], error_message.args[1]))