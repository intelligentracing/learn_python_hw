from collections import deque

def in_place_sort(input_queue, reverse = False):
    ''' sorting a deque representing a queue in place
    Parameters:
    Input:  input_queue - a deque type queue
            reverse     - boolean. ascending for False, and descending for True

    Output: input_queue - sorted queue with the same length
    '''

    if type(input_queue)!=deque:
        raise TypeError('Argument input_queue must be a deque type')

    queue_length = len(input_queue)
    sort_index = queue_length
    while sort_index > 0:
        temp = input_queue.popleft()
        for search_index in range(1, sort_index):
            if input_queue[0]<temp:
                input_queue.append(temp)
                temp = input_queue.popleft()
            else:
                input_queue.append(input_queue.popleft())
        
        for search_index in range(sort_index, queue_length):
            input_queue.append(input_queue.popleft())
        
        input_queue.append(temp)
        sort_index -= 1

input_queue = deque([7,2,3,5,6,1,9])
in_place_sort(input_queue)
print(input_queue)
