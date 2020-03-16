#第一题
## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: syntax_error.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Most popular syntax error examples

# ********  Case 1: Wrong text formatting  ********
for i in range(10):        # Error
    print(i)
else:                       # Error
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
print(math.sqrt(9))

# ********  Case 5: Call methods in the wrong type of objects  ********
String = "Hello World!"
l=list(String)
l.reverse()
print("".join(l)) 
# ********  Case 6: Use the wrong operator on variable types
List = ['abcde']
List = List + List

# ********  Case 7: Misspell a variable
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(animals[0])

# ********  Case 8: Wrong use of quotation marks
wrong_string = "Mike's story"
print(wrong_string)




#第二题
#2038是指在2038年的时候用32位会满导致时间
#把电脑时间存储改用8字节64位的形式来存储时间