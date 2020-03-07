L = ["a" , "b"] 
L1 = [ ["a" ,"b"], 2,["a","b"]]
L2 = [ L, 2, L]
print(L)
print(L1)
print(L2)
L1[0][0] = "c"#将其中两个list首个元素改为c
L2[0][0] = "c"#L = ["a" , "b"]  L2 = [ L, 2, L]与L1 = [ ["a" ,"b"], 2,["a","b"]]效果相同
print(L1)
print(L2)
string="Acadium"
L1.append(string)#分步添加
L2.extend(string)#添加整体
print(L1)
print(L2)
print(str(L))#转为字符串形式
string.join(L)#不知道为什么没用……
print(L)