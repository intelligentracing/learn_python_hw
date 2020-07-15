from collections import deque

#ex1.1
def find_flag(opt_queue,num):
    """找到num在已经排好序的opt_queue里应该放在什么位置，即flag"""
    flag = 0
    for i in range(len(opt_queue)):
        com = opt_queue.pop()
        if com > num:
            flag = i+1 #flag代表比几个数小 有flag数比较大
        opt_queue.append(com)
    return flag

def insert(opt_queue,flag,num):
    """把num插入opt_queue中"""
    new_queue=deque()
    for i in range(flag):
        new_queue.append(opt_queue.pop())
    opt_queue.append(num)
    for i in range(flag):
        opt_queue.append(new_queue.pop())
    return opt_queue

def sort_function(queue):
    """循环以上操作将未排序的queue中的每一个元素插入到在opt_queue这个已经排好序的列表中"""
    opt_queue = deque()

    for i in range(len(queue)):
        num = queue.popleft()
        flag = find_flag(opt_queue,num)
        opt_queue = insert(opt_queue, flag, num)
    return opt_queue

queue_1 = deque([2,10,1])
print(sort_function(queue_1))

#ex1.2
# def find_min_index(queue, remain):
#     """找到这个queue中的最小值"""
#     L = len(queue)
#     min_index = -1
#     min_val = float('inf')
#     for i in range(L):
#         cur = queue.popleft()
#         if cur <= min_val and i <= remain:
#             min_index = i
#             min_val = cur
#         queue.append(cur)
#     return min_index


# def insert(queue, min_index):
#     """"把最小值min_index插入到queue中"""
#     min_val = None
#     for i in range(len(queue)):
#         cur = queue.popleft()
#         if i != min_index:
#             queue.append(cur)
#         else:
#             min_val = cur
#     queue.append(min_val)


# def inplace_sort(queue):
#     """依次找到queue中的最小值第二小值等塞到列表的末尾"""
#     for i in range(1, len(queue) + 1):
#         min_index = find_min_index(queue, len(queue) - i)
#         insert(queue, min_index)

#     return queue

# input_deque = deque([1,3,2,5,7,8,6,0])
# print(inplace_sort(input_deque))


# sort_deque(input_deque)

