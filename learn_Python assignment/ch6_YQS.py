# ********  Case 1: Wrong text formatting  ********
for i in range(10):        # Error
    print(i)
else:                        # Error
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
String = ["Hello World!"]
String.reverse()

# ********  Case 6: Use the wrong operator on variable types
List = ['abcde']
List = List + ['abcde']

# ********  Case 7: Misspell a variable
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(animals[0])

# ********  Case 8: Wrong use of quotation marks
wrong_string = "Mike's story"
print(wrong_string)