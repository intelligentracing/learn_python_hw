import random
#第二题
x=int(input('请输入第一个年份：'))
y=int(input('请输入第二个年份：'))
while x<=y :
    if x/4 == x//4 :
        print(x)
    else:
        print('不是')
    x=x+1
#第三题
List1=[]
for i in range(10):
    List1.append(random.randint(0,101))
print(List1)
List1.sort()
print(List1)

