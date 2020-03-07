#ppt上问题
#第一个
string="python"
L=list(string)
S=".join(list)
str(L)=12#12=question
print(12)#['p', 'y', 't', 'h', 'o', 'n']变成字符串
#第二个
List =['a','b',5]; id(List)
List[2]='c';id(List)
list.append('d');id(List)
List.extend(List);id(List)
List.extend(List)#['a','b','5','a','b','5']
#第三个
L=[['a','b'],5,'a']
print(L[0])
id(L[0][0])=id(L[2])
print(L[-3][-1])#b
#第二项作业
L1=[['a','b'],2,['a','b']]
L=['a','b'],L2=[L,2,L]
#question1 在L1存储L1[0]和L1[2]时，这两个元素未被定义，,但在L2[0] L2[2]中，这两个元素已经被L定义了
L1[0][0]='c' 'a'='c'#L1里面就只有'a'='c'变了
L2[0][0]='c' 'a'='c'#但L2里面的两个L都变了
#question2 我认为改变L1[0][0]=a，只是改变了L1[0][0]='c'的'a'元素使它='c',但改变L2[0][0]='c',使L=c，但L已被定义['a','b']，所以这次改变就等于'c'=['a','b']=L
#第三项作业
#question1 append函数是将新元素追加到列表末尾
a=[1,2]
b=[3,4]
a.append(b)
a
[1, 2, [3, 4]]
#extend函数可以将另一个列表中的元素逐一添加到指定列表中
a=[1,2]
b=[3,4]
a.extend(b)
a
[1, 2, 3, 4]
#question2 str函数可以将数字转化为字符串，连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
