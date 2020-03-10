## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: finally.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import sys

result = None

a = "wrong input"
b = 0

try:
    result = a / b
except ZeroDivisionError:
    print("Divided by Zero. Error!")
except TypeError:
    print("TypeError in division of {{ {0} }} by {{ {1} }}.".format(a, b))
    sys.exit()
else:
    print(result)
finally:
    if result == None:
        result = 0
    
    print(result)