## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: syntax_error.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Most popular syntax error examples

# ********  Case 1: Wrong text formatting  ********
for i in range(10):       # Error
    print(i)
else                        # Error
      pass

# ********  Case 2: Misuse of brackets  ********
List = ['abc','def']       
List[1] =  List[0]             # Error

# ********  Case 3: Wrong indentation  ********
x = 0
y = 1
z = 3

# ********  Case 4: Forget to import modules  ********
import math
print(sqrt(9))

# ********  Case 5: Call methods in the wrong type of objects  ********
String = "Hello World!"
0=list(string)
0.reverse()
print(0)
# ********  Case 6: Use the wrong operator on variable types
List = ['abcde']
List = List + List

# ********  Case 7: Misspell a variable
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(animal[0])

# ********  Case 8: Wrong use of quotation marks
wrong_string = "Mike's story"
print(wrong_string)
#第二题
#问题是指在2038年会遇到千年虫问题，因为32位系统即2的32次方只能用到2038年，如果不淘汰掉并换上64位的话，时间将重回1900