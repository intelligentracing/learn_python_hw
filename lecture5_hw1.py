year1 = input("Please input the first year:") 
year2 = input("Please input the second year:") 

for i in range(int(year1)+1, int(year2) + 1):
    if i % 100 == 0:
        if i % 400 == 0: 
            print(i, end=" ")
        else: 
            continue  
    elif i % 4 == 0:
        print(i, end=" ")     
