#Midium1 ex3_String.py
#Author: Yu Qiuhsuang

orign = input('please input the orign sentence:')
test = input('please input the test sentence:')

orign = orign.replace(' ','')
orign = sorted(orign)
#orign = [s.lower() for s in orign if isinstance(s,str)==True]
test = test.replace(' ','')
test = sorted(test)
#test = [s.lower() for s in test if isinstance(s,str)==True]
if orign == test:
    is_anagram = True
else:
    is_anagram = False

print(is_anagram)