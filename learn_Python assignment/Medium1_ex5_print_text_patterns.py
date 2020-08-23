times = input('please input times range from 0 to 10:')
times = int(times)
for i in range(-7,8):
    print('*', end ='')
print()

for i in range(-7, 8):
    a = ' '	
    if i < -7 + times or i > 7-(10 -times):
        a ='.' 
    # 空格
    for j in range(7 - abs(i)):
        print(' ', end='')
    # *
    for k in range(2 * abs(i) + 1):
        if k == 0 or k == 2 * abs(i):
            print('*', end='')
        else:
            print(a, end ='')
    print()

for i in range(-7,8):
    print('*', end ='')
print()