# This is the second problem that I need to solve for this week's homework

import random 

random_integers = [] 

for i in range(10): 
    random_int = random.randint(1, 100) 
    random_integers.append(random_int)
    if i == 0:
        continue 
    elif random_int > random_integers[0:i]:
        continue 
    elif 

print(random_integers)


