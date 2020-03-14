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


def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:return []
        triangle=[[1]]
        if numRows==1: return triangle
        for i in range(1,numRows):
            tmp=[1]
            for j in range(1,i):
                tmp.append(triangle[i-1][j-1]+triangle[i-1][j])
            tmp.append(1)
            triangle.append(tmp)
        return triangle


