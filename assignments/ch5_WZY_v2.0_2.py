import math
import random
List=[]
print("How many random number do you need?")
num=input()
print("Random number start from")
start=input()
print("Random number end in")
end=input()
for i in range(0,int(num)):
    List.append(random.randint(int(start),int(end)))
print(List)
for i in range(len(List) - 1):
    for j in range(len(List)-1 - i):
        if List[j] > List[j + 1]:
            List[j], List[j + 1] = List[j + 1], List[j]
print(List)