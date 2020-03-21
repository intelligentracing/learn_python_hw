from collections import deque
from time import time 
A = deque()
B = deque()
C = deque()
m=0
def move(disks,N,M):
    return m+=1
    print("Times: " +str(m)+" put " + str(disks) +" from " + str(N) +" to " + str(M))
def hanoi (n,A,B,C):
    if n == 1:
        move(1, A, C)
    else:
        hanoi(n - 1, A, C, B)
        move(n, A, C)
        hanoi(n - 1, B, A, C)


print("Please Enter the number of the disk.")
disks = int(input())
hanoi(disks, A, B, C)
print(">>move " + m + " times,put all Disk in A to C")