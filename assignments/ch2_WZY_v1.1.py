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
     #change number into action 
    if computer_input== 1 :
         #change number into action 
         ComputerInput="Rock"
     #change number into action 
    elif computer_input == 2 :
         #change number into action 
         ComputerInput="Paper"
     #change number into action 
    else:
         #change number into action 
         ComputerInput="Scissors"
     #tell player what computer choose
    print("Computer input is ",ComputerInput)
     #find whether inputs are same
    if user_input==computer_input:
         #show player draw
         print("Draw")
     #find whether player is win
    elif user_input-computer_input==1 or user_input-computer_input==-2:
         #show player win
         print("You Win!")
     #find whether player is lose
    else:
         #find whether player is win
         print("You Lose!")