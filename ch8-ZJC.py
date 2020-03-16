#第一题
from collections import deque
queue = deque([10, 4, 5, 3, 2, 6, 7, 9, 8])
def find_min_index(queue, remain):
    L = len(queue)
    min_index = -1
    min_val = float('inf')
    for i in range(L):
        cur = queue.popleft()
        if cur <= min_val and i <= remain:
            min_index = i
            min_val = cur
        queue.append(cur)
    return min_index
def insert(queue, min_index):
    min_val = None
    for i in range(len(queue)):
        cur = queue.popleft()
        if i != min_index:
            queue.append(cur)
        else:
            min_val = cur
    queue.append(min_val)
def inplace_sort(queue):
    for i in range(1, len(queue) + 1):
        min_index = find_min_index(queue, len(queue) - i)
        insert(queue, min_index)
    return queue
print(inplace_sort(queue))
#第二题
from collections import deque
def place_sort(input_deque, reverse=False):
    for i in range(len(input_deque)):
        min=input_deque.popleft()
        for j in range(len(input_deque)-i):
            a=input_deque.popleft()
            if min<a:
                input_deque.append(a)
            else:
                input_deque.append(min)
                min=a
        for m in range(i):
            input_deque.append(input_deque.popleft())
        input_deque.append(min)
    print(input_deque)
input_deque=deque([2,15,36,4,98,5])
print(place_sort(input_deque))

        