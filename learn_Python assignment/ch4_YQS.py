#ex1.1(1)
L1 = [['a', 'b'], 2, ['a','b']]
L = ['a', 'b']
L2 = [L, 2, L]

print('L1[0]: ', L1[0])
print('L1[2]: ', L1[2])

print('L2[0]: ', L2[0])
print('L2[2]: ', L2[2])
# #ex1.1(2)
print(id(L))
L1[0][0] = 'c'
L2[0][0] = 'c'

print('L1: ', L1)
print('L2: ', L2)
print('L:', L)
print(id(L))

#ex1.2
list_1 = ['a','b','c', 4]
list_2 = ['d','e','f']
list_1copy = list_1.copy()
list_1_1 = list_1[:]
list_1.append(list_2)
print(list_1)
print(len(list_1))
list_1_1.extend(list_2)
print(list_1_1)
print(len(list_1_1))

list_3 = [20,213]
for i in list_3:
    for s in range(0,len(list_3)):
    list_3[s] = str(i)
print(list_3)
result = ' '.join(list_3)
print(result)
