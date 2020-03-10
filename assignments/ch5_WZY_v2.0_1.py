print("please enter the start year.")
startYear=input()
print("please enter the end year.")
endYear=input()
if(startYear<endYear):
    List =[]
    for temp in range(int(startYear),int(endYear)+1):
        if ((temp%100==0 and temp%400==0) or temp%4==0):
            List.append(temp)
    print("The leaf years are:"+str(List))
else:
    print("Invaid input, please check again.")