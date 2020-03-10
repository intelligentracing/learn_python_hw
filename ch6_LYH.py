## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: syntax_error.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Most popular syntax error examples

# ********  Case 1: Wrong text formatting  ********
while i in range(10):        # Error
    print(i)
else:                        # Error
    pass

# ********  Case 2: Misuse of brackets  ********
 List = ['abc','def']        
 print(List[1])             # Error

# ********  Case 3: Wrong indentation  ********
x = 0
y = 1
z = 3

# ********  Case 4: Forget to import modules  ********
import math
print(sqrt(9))

# ********  Case 5: Call methods in the wrong type of objects  ********
String = "Hello World!"


# ********  Case 6: Use the wrong operator on variable types
List = ['abcde']
List = 'abcde'

# ********  Case 7: Misspell a variable
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(animals[0])

# ********  Case 8: Wrong use of quotation marks
wrong_string = 'Mike"s story'
print(wrong_string)
#第二项作业
2038年问题是指在使用POSIX时间的32位计算机应用程序上，格林尼治时间2038年1月19日凌晨03:14:07（北京时间：2038年1月19日中午11:14:07）之后无法正常工作。
解决方案 只要给那些程序换一个新版本的“标准时间库”就可以了，比如说，改用8字节64位的形式来存储时间