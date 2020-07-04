# For the first problem I copy pasted syntax_error.py and modified/fixed all of the errors 

# ********  Case 1: Wrong text formatting  ******** --> FIXED
for i in range(10):        
    print(i)
else:                        
      pass

# ********  Case 2: Misuse of brackets  ******** --> FIXED
List = ['abc','def']        
List[1] =  List[0]             # Error

# ********  Case 3: Wrong indentation  ******** --> FIXED
x = 0
y = 1
z = 3

# ********  Case 4: Forget to import modules  ******** --> FIXED
import math 
print(math.sqrt(9))

# ********  Case 5: Call methods in the wrong type of objects  ******** --> FIXED
String = list("Hello World!")
String.reverse()
print(String)

# ********  Case 6: Use the wrong operator on variable types --> FIXED
List = 'abcde'
List = List + 'abcde'
print(List)
# ********  Case 7: Misspell a variable --> FIXED
animals = ['dog', 'cat', 'pony', 'fisn', 'leopard', 'rabbit','mouse']
print(animals[0])

# ********  Case 8: Wrong use of quotation marks --> FIXED
wrong_string = 'Mike"s story'
print(wrong_string)