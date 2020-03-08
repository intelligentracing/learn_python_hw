import random
#第二题
x=int(input('请输入第一个年份：'))
y=int(input('请输入第二个年份：'))
w=0
List=[]
while x<=y :
    if x/4 == x//4 :
        List.append(x)
    x=x+1
print(List)
while w<=len(List)-1:
    if List[w]/100==List[w]//100 and List[w]/100/4!=List[w]//100//4:
        List.remove(List[w])
    w=w+1
print(List)
#第三题
List1=[]
for i in range(10):
    List1.append(random.randint(0,101))
print(List1)
List1.sort()
print(List1)

