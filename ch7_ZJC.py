#第一题（1）
import time
import random
def merge_sort(input_list,reverse=False):
        # Deploy Divide-and-Conquer
    if type(reverse)!=bool:#检查
        return False
    if reverse==False:
        if len(input_list)>1:
            if type(input_list)!=list:#检查
                return False
            mid = len(input_list)//2
            left_half = input_list[:mid]
            right_half = input_list[mid:]
            merge_sort(left_half)
            merge_sort(right_half) 
            i=0
            j=0
            k=0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    input_list[k]=left_half[i]
                    i=i+1
                else:
                    input_list[k]=right_half[j]
                    j=j+1
                k=k+1

            while i < len(left_half):
                input_list[k]=left_half[i]
                i=i+1
                k=k+1

            while j < len(right_half):
                input_list[k]=right_half[j]
                j=j+1
                k=k+1
    if reverse==True:
        if len(input_list)>1:
            mid = len(input_list)//2
            left_half = input_list[:mid]
            right_half = input_list[mid:]
            merge_sort(left_half)
            merge_sort(right_half) 
            i=0
            j=0
            k=0
            while i <len(left_half) and j<len(right_half):
                if left_half[i]>=right_half[j]:
                    input_list[k]=left_half[i]
                    i=i+1
                else:
                    input_list[k]=right_half[j]
                    j=j+1
                k=k+1
            while i < len(left_half):
                input_list[k]=left_half[i]
                i=i+1
                k=k+1

            while j < len(right_half):
                input_list[k]=right_half[j]
                j=j+1
                k=k+1
sample_count = 10000
random_input = random.sample(range(0, sample_count),sample_count)
print('*** Merge Sort ***')
result = random_input.copy()
begin_time = time.time()
merge_sort(result)
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])

#第二题
def triangles():
    L = [1]
    while True:
        yield L
        L = [L[0]] + [(L[i] + L[i + 1]) for i in range(len(L) - 1)] + [L[-1]]
 
n =0
w=int(input())
for t in triangles():
    print(t)
    n = n + 1
    if n>=w :
        break