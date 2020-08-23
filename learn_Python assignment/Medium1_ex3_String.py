orign = input('please input the orign sentence:')
test = input('please input the test sentence:')

orign = orign.replace(' ','')
orign = sorted(orign)
orign = [s.lower() for s in orign if isinstance(s,str)==True]
test = test.replace(' ','')
test = sorted(test)
test = [s.lower() for s in test if isinstance(s,str)==True]

all = [x for x in orign if x in test]
result = [y for y in (orign + test) if y not in all]

if len(result) == 0:
    is_anagram = True
else:
    is_anagram = False

print(is_anagram)