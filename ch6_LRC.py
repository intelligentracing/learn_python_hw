#和21世纪初的千年虫(the Millennium bug)问题类似，32位的Unix操作系统和Linux操作系统时间溢出问题又称为2038年问题(the Year 2038 problem)。如果你想知道什么是2038问题的话，你需要知道一些技术上的东西。这个bug是由用来写Unix/Linux的C语言引起的，C语言中用 time_t 来代表时间和日期，time_t 是整数(int)型的，它用来记载从1970年1月1日到2000年所经历的秒数。
#这个数据是以32位存储的，第一位是符号位，其余的31位用来存数字，而这31位数字可以存储的最大数字为2147483647。
#从1970年开始计算，这31位的数字可以表示的秒数最多可以用到2038年01月19日03时14分07秒，当时间到达这个数字的时候系统将会出现问题，到时候数字不会自动增加，而是会变为-2147483647，而这串数字代表的时间是1901年12月13日20时45分52秒，这会导致很多的程序出现问题，甚至崩溃。
#2038年问题不仅比千年虫更隐蔽，而且比之前千年虫问题更具有破坏力，因为千年虫问题只会导致应用层的程序出现问题，比如信用卡支付系统，或者管理系统。而2038这个bug，将会影响系统最底层的时间控制的功能。
#要解决这个问题，最简单的方式是扩展Unix时间的长度，用64位数字来表示它。64位二进制数的实际可用位数是63位，最大表示到公历的UTC时间292,277,026,596年12月4日15时30分08秒. 如果那个时候人类文明还存在的话，公元纪年很可能已经因为太难用而被抛弃了. 理想的情况是到2038年，64位系统已经成为主流，从而避免特意去修正这个问题所需要的大量开销。否则，人们就必须把新的64位时间拆分成两部分并分别保存在两个变量里，这是一个麻烦而且效率低下的选择.
#____________________________________
## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: syntax_error.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Most popular syntax error examples

# ********  Case 1: Wrong text formatting  ********
for i in range(10)        # Error
    print(i)
else                        # Error
    pass

# ********  Case 2: Misuse of brackets  ********
List = ('abc','def')        
List(1) =  List(0)             # Error

# ********  Case 3: Wrong indentation  ********
x = 0
y = 1
z = 3

# ********  Case 4: Forget to import modules  ********
import math print(math.sprt(9))
print(sqrt(9))
# ********  Case 5: Call methods in the wrong type of objects  ********
String = "Hello World!"
print("string")

# ********  Case 6: Use the wrong operator on variable types
List = ['abcde']
List = List + List
# ********  Case 7: Misspell a variable
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(animal[0])

# ********  Case 8: Wrong use of quotation marks
wrong_string = "Mike's story"
print(wrong_string)
