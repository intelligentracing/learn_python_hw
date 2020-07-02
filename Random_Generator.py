import math
import random

List = list("Python")
numberslist = []
temporaryList = []
counter = 0
for x in range (0,9):
    temporaryList.append(random.randrange(0,100)) ## creating the 10 numbers

temporaryList.sort()
print (temporaryList)


