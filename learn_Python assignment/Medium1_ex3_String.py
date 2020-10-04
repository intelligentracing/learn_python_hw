#Midium1 ex3_String.py
#Author: Yu Qiuhsuang

orign = input('please input the orign sentence:')
test = input('please input the test sentence:')

orign = orign.replace(' ','')
orign = sorted(orign)
orign = [s.lower() for s in orign if isinstance(s,str)==True]
test = test.replace(' ','')
test = sorted(test)
test = [s.lower() for s in test if isinstance(s,str)==True]
# test_result = []
# for s in test:
#     if isinstance(s, str) == True:
#         test_result.append(s.lower()) 
all = [x for x in orign if x in test]
result = [y for y in test if y not in all]

if len(result) == 0:
    is_anagram = True
else:
    is_anagram = False

print(is_anagram)