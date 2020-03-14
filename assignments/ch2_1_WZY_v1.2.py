#rock_paper_scissors
import random

print("Please input [1] Rock,[2] Paper, or [3]Scissors")#要求输入1，2，3
user_input = int(input())#请求输入
if user_input !=1 and user_input !=2 and user_input !=3:#如果用户输入不是1，2，3
     print("Input not supported")#告知无法识别输入
else:#如果用户输入是1，2，3
     computer_input =random.randint(1,3)#电脑随机生成1，2，3
     if computer_input== 1 : #如果输入为1
          ComputerInput="Rock" #电脑输入为石头
     elif computer_input == 2 :#如果输入为2
          ComputerInput="Paper"#电脑输入为剪刀
     else: #其他输入（输入为3）
          ComputerInput="Scissors" #电脑输入为剪刀
     print("Computer input is ",ComputerInput) #告知用户电脑输入为
     if user_input==computer_input:#如果用户输入和电脑输入相等
          print("Draw")#告知平局
    elif user_input-computer_input==1 or user_input-computer_input==-2:#如果用户输入赢了电脑输入
         print("You Win!")#告知胜利
    else:#如果用户输入输了电脑输入
         print("You Lose!")#告知失败