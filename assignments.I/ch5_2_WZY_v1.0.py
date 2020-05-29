import math
import random
List=[]
FinalList=[]
print("Random number is from 0~100")
num=0
while (num<10):
    List.append(random.randint(0,100))
    num+=1
index=10
print(List)
time=0
while (time<index):
    tempmin=List[time]
    temp=time
    remove=temp
    while (temp<index):
        if(tempmin>List[temp]):
            tempmin=List[temp]
            remove=temp
        temp+=1
    List.remove(List[remove])
    FinalList.append(tempmin)
    index-=1
print(str(FinalList))