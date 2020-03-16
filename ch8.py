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