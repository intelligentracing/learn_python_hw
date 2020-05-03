# QUEUE AND STACK
# When using collections.deque class, one can implement both a queue data 
# structure using deque.append() and deque.popleft() or a stack data structure 
# using deque.append() and deque.pop(). However, using a recursive function, 
# one can implement the queue function of dequeue (that is, popleft) only 
# using the stack operations of append() and pop(). Design an implementation 
# of such a function.
from collections import deque
def magic(a):
    
    if len(a)==1:
        print(a.pop())
       
    else:
        a.pop()
        magic(a)

a=deque([1,2,3,4,5])
magic(a)