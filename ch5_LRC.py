for i in range(2000,2501):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)
    else:
    	print("It is wrong")
#-————————————————————分割线————————————————————-
import random

list_1 = []
for i in range(10):
	list_1.append(random.randint(0,100)
print('生成的随机整数列表为：\n',list_1)
def insert_sort(list_1):
    for i in range(len(list_1)-1):
        if list_1[i+1]<arr[i]:
            for j in range(i+1,0,-1):
                if list_1[j]<list_1[j-1]:
                    list_1[j-1],list_1[j]=list_1[j],list_1[j-1]
                else:
                    break
    return list_1
print('排序后的列表为：\n',list_1)
