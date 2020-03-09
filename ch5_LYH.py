#ex2
leap_years=[]
The_year1=input('please provide an integer limit to finding leap year:')
The_year2=input('please provide an integer limit to finding leap year:')
try:
    The_year=int(The_year)
except:
    print('Not a valid integer input. Exit')
else:
     for year1 in range(0,The_year+1):
      if (year1 % 4 == 0 and year1 % 100 != 0) or year1 % 400 == 0:
        leap_years.append(year1)
        print(leap_years)
   
#ex3
import random
num=random.sample(range(0,100),10)
num.sort()
print(num)
