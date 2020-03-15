def merge_sort(input_list,reverse):
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
        merge_sort(left_half,reverse)
        merge_sort(right_half,reverse)

        # Merging left_half and right_half 
    for x in input_list:
        if type(int(x))!=int:
            return ("list type invalid, please check input again.")
            break
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
    if reverse=="True":
        return input_list.reverse
    elif reverse=="False":
        return input_list
    else:
        return ("reverse invalid, please check input again.")


print("type in whatever you like, end with .")
end=0
list=[]
while(end<1): 
    temp=input()
    if(temp!="."):
        list.append(temp)
    else:
        end+=1
print("reverse or not? True for reverse, False for not.")
ron=input()
print(str(merge_sort(list,ron))) 