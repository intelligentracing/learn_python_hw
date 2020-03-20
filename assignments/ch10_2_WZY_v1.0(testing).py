import math

def fibonacci (i):
   return int(((math.sqrt(5)-1)/2)**(-i))

print("Which one you need?")
i=int(input())
print(str(fibonacci(i)))