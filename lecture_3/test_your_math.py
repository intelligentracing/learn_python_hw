## This is course material for Introduction to Python Scientific Programming
## Class 3 Example code: test_your_math.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use


# import two Python modules
import random   # includes functions for generating random numbers
import math     # includes additional math functions

# Define constants
OPERATOR_ROUND = 1
OPERATOR_INT = 2
OPERATOR_FLOOR = 3
OPERATOR_CEIL = 4

random_operator = random.randint(1,4)   # Select an operator randomly
random_A = random.randint(-10,10)       # Select first value randomly
random_B = random.randint(-10,10)       # Select second value randomly
if random_operator == OPERATOR_ROUND:   # If selected operator is round()
    result = round(random_A/random_B)
    operator_string = "round"
elif random_operator == OPERATOR_INT:   # If selected operator is int()
    result = int(random_A/random_B)
    operator_string = "int"
elif random_operator == OPERATOR_FLOOR: # If selected operator is floor()
    result = math.floor(random_A/random_B)
    operator_string = "floor"
else:                                   # If selected operator is ceil()
    result = math.ceil(random_A/random_B)
    operator_string = "ceil"

# Prepare question string
question_string = ( "Question: " + operator_string + "(" + str(random_A) 
                    + "/" + str(random_B) + ") = ? ")
user_result = \
    input(question_string)    # Wait for user input 
user_result = int(user_result)          # Convert string to int
if  user_result == result:              # The answer is correct, add one score
    print("Correct!")
else:           # The answer is wrong, add one score
    print("Incorrect!")