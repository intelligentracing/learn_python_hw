import time

def fun(number,x,y,z,process): # 汉诺塔的实现方法，会将步骤依次输出（核心）
    if number==1:
        process.append([x,z])
    else:
        fun(number-1,x,z,y,process)  # 前n-1个盘子借助z由x移动到y
        process.append([x,z])    # 打印出第n个盘由x移向z
        fun(number-1,y,x,z,process)  # 前n-1个盘子借助x由移到z上

def myhun(a): #将fun方法中的步骤整合成一个过程（list）
    process=[]
    number = a
    fun(number,0,1,2,process)
    return process


def panzi(x):#生成盘子以及柱子，盘子以数字表示，数字大表示盘子在相对下方的位置
    pillar1 = []
    pillar2 = []
    pillar3 = []
    for a in range(1,x+1):
        pillar1.append(a)
        pillar1.sort()
    pillar=[pillar1,pillar2,pillar3]
    return pillar

def move(z,y):#使myhun方法中的过程对盘子进行操作
    for c in range(0,len(y)):
        number = z[y[c][0]][0]
        z[y[c][1]].insert(0,number)
        del z[y[c][0]][0]
        print(z)

def khd():#整合用户输入并实现move方法
    int (input("输入圆盘数量"))
    move(panzi(5),myhun(5))

khd()#方法实现
'''整个方法以更形象的方式输出，其中核心方法部分从网上借鉴。
   输出的值为一行一个list，即为步骤，每个list中的三个list
   为三个柱子。'''


t_1=time.time()
def fib(n):
    f=[0,1]
    for a in range(2,n):
        f.append(f[a-2]+f[a-1])
    return f[n-1]

print(fib(30))
t_2=time.time()
t_end=t_2-t_1
print(t_end)
