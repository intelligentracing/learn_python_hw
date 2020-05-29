import random  
import math    
import time

# Define constants
OPERATOR_ROUND = 1
OPERATOR_INT = 2
OPERATOR_FLOOR = 3
OPERATOR_CEIL = 4

score = 0
print("*** Test Your Math: How Fast Can You Score 10 ***")
begin_time = time.time()
while score<10:
    random_operator = random.randint(1,4)   
    random_A = random.randint(-10,10)       
    random_B = random.randint(-10,10)      
    if random_operator == OPERATOR_ROUND: 
        result = round(random_A/random_B)
        operator_string = "round"
    elif random_operator == OPERATOR_INT: 
        result = int(random_A/random_B)
        operator_string = "int"
    elif random_operator == OPERATOR_FLOOR:
        result = math.floor(random_A/random_B)
        operator_string = "floor"
    else:                               
        result = math.ceil(random_A/random_B)
        operator_string = "ceil"

   
    question_string = "Question: " + operator_string + "(" + str(random_A) + "/" + str(random_B) + ") = ? "
    user_result = input(question_string)   
    user_result = int(user_result)        
    if  user_result == result:
        score = score + 1                  
        print("Correct! Your score increases to ", score)
    else:
        score = score - 1                 
        print("Incorrect! Your score decreases to ", score)

elapsed_time = time.time()-begin_time
print("You spent %.2f seconds" % elapsed_time)