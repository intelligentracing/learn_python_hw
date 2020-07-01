# This is the second problem that I need to solve for this week's homework
# This question asks us to sort in ascending orders random integers from 1-100

# This is the first solution using .sort() method 
import random 



def sort_random_list():
    random_list = random.sample(range(0, 100), 10)
    random_list.sort()  
    print(random_list)
    return 

sort_random_list() 

# This is the second method using sorted()- With this way we have to assign sorted() to a variable then we
# need to print the variable 

def sort_random_list2():
    random_list2 = random.sample(range(0, 100), 10)
    a = sorted(random_list2)  
    print(a)
    return 

sort_random_list2() 
