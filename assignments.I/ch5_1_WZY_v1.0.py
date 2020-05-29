print("please enter the start year.")
startYear=input()
print("please enter the end year.")
endYear=input()
if(startYear<endYear):
    List =[]
    Index=int(endYear)-int(startYear)
    temp=int(startYear)
    while(temp<=int(endYear)):
        if(temp%4==0):
            List.append(temp)
        temp=temp+1
    print("The leaf years are:"+str(List))
else:
    print("Invaid input, please check again.")