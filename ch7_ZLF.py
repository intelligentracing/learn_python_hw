import random
import time


def merge_sort(input_list,reverse=False):
 
    # Deploy Divide-and-Conquer
    if len(input_list)>1:
        mid = len(input_list)//2
        left_half = input_list[:mid]
        right_half = input_list[mid:]

        # Recursively sort left and right sub-lists
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging left_half and right_half 
        i=0
        j=0
        k=0
        if reverse==True:
            while i < len(left_half) and j < len(right_half):
                if left_half[i] >= right_half[j]:
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

        else:
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


# Generate a sufficiently long list for sorting
sample_count = 10000
random_input = random.sample(range(0, sample_count),sample_count)



# ******** Method 2: Merge Sort ********
print('*** Merge Sort ***')
result = random_input.copy()
begin_time = time.time()
merge_sort(result)

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])


def triangle(List,n=10):
    if len(List)<=n:
        List1=List.copy()
        List=[]
        if List1!=[]:
            List.append(1)
            for x in range(0,len(List1)-1):
                List.append(List1[x]+List1[x+1])
            List.append(1)
            for n in range(0,n-len(List1)+25):
                print(" ",end="")
            print(List)

        else:
            List = List1 =[1]
            for x in range(0,n-len(List1)+25):
                print(" ",end="")
            print(List)
        triangle(List)
    

triangle([],11)

