#rock_paper_scissors
import random

#ask user to input P or S or R
print("Please input [1] Rock,[2] Paper, or [3]Scissors")
#ask for user input
user_input = int(input())
#if user put illegal argument
if user_input !=1 and user_input !=2 and user_input !=3:
     #reject the input
    print("Input not supported")
#other legal statement
else:
     #get computer random input
    computer_input =random.randint(1,3)
    print("Computer input is ",computer_input)
    if user_input==computer_input:
         print("Draw")
    elif user_input-computer_input==1 or user_input-computer_input==-2:
         print("You lose!")
    else:
         print("You win!")