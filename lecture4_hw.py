#Ex1.1

L1 = [['a', 'b'],2,['a', 'b']]
L = ['a', 'b']
L2 = [L, 2, L] 

# a) 
print(L1[0], L1[2]) 
print(L2[0], L2[2]) 
# The difference observed seems to be that L2 stores ['a', 'b'] with var. L instead, though results are same

# b)
L1[0][0] = 'c'
L2[0][0] = 'C'
print(L1, L2) 
# with L1 it changes index 0 of index 0, which only affects 'a' in index 0 in the list 
# with L2 its affecting index 0 of index 0 in the list, which technically means its affecting var. L,
# meaning that not only will 'a' in the list index0 turn into 'C', but index 2 in L2 will also turn into 
# a list with a 'C' instead of 'a', since var. L is found in index 0 and index 2 in L2, changing both

# Ex1.2 

#a) string.append adds one element to the end of string. string.extend adds as many elements to the end of 
# string 

#b) str(List) converts all of the content in List to be a string. ''.join(List) forms one big string out of
# all of the contents inside List, with essentially nothing spaced between them, judging from the empty 
# quotation marks
