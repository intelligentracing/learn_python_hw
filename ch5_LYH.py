#ex2
leap_years=[]
The_year=input('please provide an integer limit to finding leap year:')
try:
    The_year=int(The_year)
except:
    print('Not a valid integer input. Exit')
else:
     for year1 in range(0,The_year+1):
      if (year1 % 4 == 0 and year1 % 100 != 0) or year1 % 400 == 0:
        leap_years.append(year1)
        print("这是闰年")
        print(leap_years)
      else:
        print("这不是闰年")
#ex3
for number in range(0,101):
    print(number)
    print(number)
    print(number)
    print(number)
    print(number)
    print(number)
    print(number)
    print(number)
    print(number)
    print(number)
