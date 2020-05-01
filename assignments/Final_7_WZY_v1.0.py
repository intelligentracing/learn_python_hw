# 1D NN ALGORITHM
# In 1D case, given a list of float elements and a query element, find the 
# nearest neighbor of the query element in the list. Further, use time.time() 
# method to compare how to improve the speed performance between:
# (1) Find nearest neighbor from an un-sorted list, and (2) Find nearest 
# neighbor from a sorted list.
# Can we find algorithms to have faster search speed when the list has 
# been sorted in the second scenario?
import random
import time

def sorted_list_nn(a,ele):
    if a[0]>ele :
        return a[0]
    if a[-1]<ele:
        return a[-1]
    for i in range(len(a)-1):
        if a[i+1]>ele>=a[i]:
            # print(a[i],a[i+1])
            if abs(a[i]-ele)>abs(a[i+1]-ele):
                return a[i+1]
            else:
                return a[i]

def unsorted_list_nn(a,ele):
    temp=float("inf")
    for i in a:
        if abs(ele-temp)>abs(ele-i):
            temp=i
    return temp
            
testlist=[]
sample_num=1000000
pointer=0
while pointer<sample_num:
    testlist.append(random.randint(0,1000000000))
    pointer+=1
result=0
# print(testlist)
starttime=time.time()
result=unsorted_list_nn(testlist,1428)
print(result)
print("duration: ",time.time()-starttime)
testlist.sort()
# print(testlist)
starttime0=time.time()
result=sorted_list_nn(testlist,1428)
print(result)
print("duration: ",time.time()-starttime0)
