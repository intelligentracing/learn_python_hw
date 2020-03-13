#第一项
# def merge_sort(input_list):
    ''' Merge sort function using recursion
    Parameters:
    Input:  input_list  - a list of numerical numbers

    Output: input_list  - sorted list
    '''
    
    # Deploy Divide-and-Conquer
    if type(reverse)!=bool
        return False
       
    if len(input_list)>1:
        mid = len(input_list)//2
        left_half = input_list[:mid]
        right_half = input_list[mid:]

        # Recursively sort left and right sub-lists
        merge_sort(left_half，reverse=true)
        merge_sort(right_half,reverse=true)

        # Merging left_half and right_half 
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
# Generate a sufficiently long list for sorting
sample_count = 10000
random_input = random.sample(range(0, sample_count),sample_count)

# ******** Method 1: Insert Sort ********
print('*** Insert Sort ***')
result = random_input.copy()
begin_time = time.time()
insert_sort(result, True)

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])

# ******** Method 2: Merge Sort ********
print('*** Merge Sort ***')
result = random_input.copy()
begin_time = time.time()
merge_sort(result)

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])

# ******** Method 3: Built-in Timsort ******
print('*** Python Sort ***')
result = random_input.copy()
begin_time = time.time()
result.sort()

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])


#第二项

def triangles():
    L = [1]
    while True:
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
