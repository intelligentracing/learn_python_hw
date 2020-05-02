'''利用堆栈的性质构建popleft方法。注：暂时未使用递归，
且popleft后原list为popleft的返回值（bug），暂未解决。'''

def popleft(alist):
    lIST = []
    for a in range(len(alist)-1):
        current_number = alist.pop()
        lIST.append(current_number)
    popnumber = alist[0]
    lIST.reverse()
    alist = lIST
    return popnumber

List = [2,2,3,5]
print(popleft(List))

