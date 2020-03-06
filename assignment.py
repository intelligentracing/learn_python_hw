#第一题
List=['a','b',5]; print(List)
List[2]='c'; print(List)
List.append('d'); print(List)
List.extend(List); print(List)
string="Python"
L=list(string)
print(str(L))
#第二题
L1=[['a','b'],2,['a','b']]
L=['a','b']; L2=[L,2,L]
#(1)L1储存L1[0],L1[2]时是一个多层表，而L2储存L2[0],L2[2]是两个变量能直接通过L该内容，更加方便
L1[0][0]='c'
print(L1)
L2[0][0]='c'
print(L2)
#(2)因为在L1中[0],[2]是独立的所以[0]的改变不会影响[2],但L2中[0],[2]是同一个变量所以[0]中[0]变了，[2]也会一起变
#第三题
string=['1','2','3','4']
string.append('5'); print(string)
string.extend(string); print(string)
#append(X)是将X加在列表的最后边，而extend则是将列表的内容扩大一倍，也就是重复了一遍列表里的内容
string="123"
List=list(string)
O='5'.join(List)
print(O)
D=str(List)
print(D)
#'X'.join(List)是在每两个内容的中间加上X，而str(List)是将列表强转为字符串