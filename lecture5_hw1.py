# This is the first problem I need to do for this weeks homework 
# Essentially I need to output the leap years inbetween the 2 years that the user inputs 

year1 = input("Please input the first year:") 
year2 = input("Please input the second year:") 
def leapyear():
    if year2 < year1: 
        print("Sorry, unfortunately your first year has to smaller than your second year.")
        return 
    for i in range(int(year1)+1, int(year2)):
        if i % 100 == 0:
            if i % 400 == 0: 
                print(i, end=" ")
            else: 
                continue  
        elif i % 4 == 0:
            print(i, end=" ")     
    return  

leapyear() 