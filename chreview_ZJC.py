#第一题
def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)
        print(x,"-->",y)
        hanoi(n-1,y,x,z)
while True:
    n=int(input("请输入汉诺塔的层数："))

    hanoi(n,"x","y","z")
#第二题
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(30):
    print(i)