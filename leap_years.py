import math
import sys
List = list("Python")
leapyearslist=[]
int_limit = int(input("Provide an integer to be the starting year "))
int_limit2 = int(input("Provide another integer to be the ending year "))
temporary1 = int_limit ## First Year Value
temporary2 = int_limit2 ## Second Year Value
if(temporary1 > temporary2):
    temp = temporary1
    temporary1 = temporary2
    temporary2 = temp ##To make sure that the first year value is the lower number.
while(temporary1 <= temporary2):
    if(temporary1  % 4 == 0): ##checking if it is a leap year
        temporary = temporary1
        leapyearslist.append(temporary)
    temporary1 = (temporary1 + 1)

print (leapyearslist)
    
        