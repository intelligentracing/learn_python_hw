lst = [4,5,6,3,2,1]
#print(insert_sort(lst))

def insertSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr
print(insertSort(lst))
#-------------------------
def insert_sort(list):
    for i in range(1,len(list)): 
        for j in range(i):  
            if(list[i]<list[j]):
                list[i],list[j]=list[j],list[i] 
    return list
print(insert_sort(list))
