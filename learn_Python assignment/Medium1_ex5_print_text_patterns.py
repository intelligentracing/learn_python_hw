times = input('please input times range from 0 to 10:')
times = int(times)
for i in range(-10,11):
    print('*', end ='')
print()
#整个沙漏从上向下一行一行打印，从-10，打印到10，从上向下每一行依次是-10， -9， -8，......
for i in range(-10, 11):
    a = ' '	
    if i < -10 + times or i > 10-(10 -times):
        a ='.' 
    # 最前边的空格
    for j in range(10 - abs(i)):
        print(' ', end='')
    # *
    for k in range(2 * abs(i) + 1):
        #首尾的*
        if k == 0 or k == 2 * abs(i):
            print('*', end='')
        else:
            #中间的*
            print(a, end ='')
    print()

for i in range(-10,11):
    print('*', end ='')
print()