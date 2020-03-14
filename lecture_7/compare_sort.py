## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: compare_sort.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import random
import time

def insert_sort(input_list, reverse = False):
    ''' A custom function to sort number sequences using insert sort
    Parameters:
    Input:  input_list  - Expecting a list of numerical numbers
            order       - Ascending or descending order, default = 0

    Output: status      - Boolean: True or False
            input_list  - sorted list if status is True
    '''
    if type(reverse)!=bool:
        return False

    for index in range(len(input_list)):
    
        # Compare and sort elements one by one
        current = input_list[index]

        # Verify the type of each element
        if type(current)!=int and type(current)!=float:
            return False

        # Insert to previous sorted sub-list
        # Insert condition based on order
        if reverse == 0:
            while_condition = (index>0 and input_list[index-1]>current)
        else:
            while_condition = (index>0 and input_list[index-1]<current)
        while while_condition:
            # Insert iteratively until insert condition is False
            input_list[index] = input_list[index-1]
            input_list[index-1] = current
            index -=1
            if reverse == 0:
                while_condition = (index>0 and input_list[index-1]>current)
            else:
                while_condition = (index>0 and input_list[index-1]<current)
    
    return True

def merge_sort(input_list):
    ''' Merge sort function using recursion
    Parameters:
    Input:  input_list  - a list of numerical numbers

    Output: input_list  - sorted list
    '''
    
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