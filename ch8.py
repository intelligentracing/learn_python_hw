from collections import deque

def sort_deque(input_deque, reverse = False):
    ''' a sorting algorithm for deque treated as an FIFO queue
    Solution uses recursing merging 1 and (n-1) queues
    parameters:
    Input:  input_deque - a deque type 
            reverse     - bool type, ascending by default False, descending by True
    
    Output: input_queue - return sorted values
    '''

    if type(input_deque)!=deque or type(reverse)!=bool:
        raise TypeError('Input arguments are not allowed.')

    if len(input_deque)==1:
        return input_deque
    
    first = input_deque.popleft()               # pop the first element
    sorted_deque = sort_deque(input_deque)      # recursively sort the (n-1) elements

    # Merge first and sorted_deque into one return deque
    new_deque = deque()
    while len(sorted_deque)>0:
        k_element = sorted_deque.popleft()
        if first <  k_element:
            new_deque.append(first)
            new_deque.append(k_element)
            break
        else:
            new_deque.append(k_element)
    else:
        new_deque.append(first)     # if while never breaks, first should be the last

    while len(sorted_deque)>0:      # After break, if any elements left in sorted_deque
        k_element = sorted_deque.popleft()
        new_deque.append(k_element)
        
    return new_deque

input_deque = deque([7,2,3,6,4,1,5])
print(sort_deque(input_deque))

def insert_sort_deque(input_deque):
    bigger_numbers=deque()
    smaller_numbers=deque()
    target_number=input_deque.popleft()
    while input_deque!=deque([]):
        try:
            compared_number=input_deque.popleft()
            if target_number>compared_number:
                smaller_numbers.append(compared_number)
            else:
                bigger_numbers.append(compared_number)
        except:
            break
    for a in range(0,len(smaller_numbers)) :
        input_deque.append(smaller_numbers.popleft())           
    input_deque.append(target_number)
    for a in range(0,len(bigger_numbers)):
        input_deque.append(bigger_numbers.popleft())
    insert_sort_deque(input_deque)

insert_sort_deque(deque([1,4,3,2,5,7,9,8,6,0]))