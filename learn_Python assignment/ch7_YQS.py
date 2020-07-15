import random

# ex1.1
def merge_sort(input_list,reverse = False):
    ''' Merge sort function using recursion
    Parameters:
    Input:  input_list  - a list of numerical numbers

    Output: input_list  - sorted list
    '''

    # Deploy Divide-and-Conquer
    if type(reverse)!=bool and type(input_list) != list:
        return False
    if reverse == False:
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left_half = input_list[:mid]
            right_half = input_list[mid:]

            # Recursively sort left and right sub-lists
            merge_sort(left_half)
            merge_sort(right_half)

            # Merging left_half and right_half
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    input_list[k] = left_half[i]
                    i = i + 1
                else:
                    input_list[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                input_list[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                input_list[k] = right_half[j]
                j = j + 1
                k = k + 1
    elif reverse == True:
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left_half = input_list[:mid]
            right_half = input_list[mid:]

            # Recursively sort left and right sub-lists
            merge_sort(left_half,reverse=True)
            merge_sort(right_half,reverse=True)

            # Merging left_half and right_half
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] >= right_half[j]:
                    input_list[k] = left_half[i]
                    i = i + 1
                else:
                    input_list[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                input_list[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                input_list[k] = right_half[j]
                j = j + 1
                k = k + 1

sample_count = 20
random_input = random.sample(range(0, sample_count),sample_count)

# ******** Method: Merge Sort ********
print('*** Merge Sort ***')
list1 = [1,3,2,4]
#list1 = random_input.copy()
merge_sort(list1,reverse=True)
print(list1)

#ex1.2
# def pascal_triangle(x,y):
#     '''x:第几行
#        y:第几个数
#        '''
#     if x == 1 and y == 1:
#         return 1
#     elif x < 1 or y < 1:
#         return 0
#     else:
#         return pascal_triangle(x - 1, y - 1) + pascal_triangle(x - 1, y)
# N = 11
# for x in range(1, N + 1):
#     for y in range(1, N - x + 1):
#         print("", end=' ')
#     for z in range(1, x + 1):
#         print(pascal_triangle(x, z),"",end=" ")
#     print()
