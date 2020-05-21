# CHECKMATE
# On a 4-by-8 half chess board, design a mini-game that lets the computer to 
# checkmate the human player. The rules are as follows:
# 1. The human plays the White King, which can move one-step at a time to any 
# of the 8 directions around the current position. The King starts at position 
# [0, 0]. The user inputs every move using the keyboard in the terminal.
# 2. The computer plays a Black Knight. The Knight starts at position [3, 7].
# 3. The computer’s goal is to use the minimal number of steps to checkmate 
# the human. At the same time, the Knight can not be placed adjacent to the 
# King, otherwise the King will capture the Knight and the computer will lose.
# User the terminal print function to update the board situation about the 
# current positions of the two pieces after each human move and computer move, 
# respectively.
## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: knight_path_DFS.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: knight_path_DFS.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque
import random
import math

knight_moves = [[-2,-1], [-1,-2], [1,-2],[2,-1], [2,1], [1,2], [-1,2], [-2,1]]
bishop_moves = [[1,1],[-1,1],[1,-1],[-1,-1],[2,2],[-2,2],[2,-2],[-2,-2],[3,3],[-3,3],[3,-3],[-3,-3],\
                [4,4],[-4,4],[4,-4],[-4,-4],[5,5],[-5,5],[5,-5],[-5,-5],[6,6],[-6,6],[6,-6],[-6,-6],\
               [7,7],[-7,7],[7,-7],[-7,-7],[8,8],[-8,8],[8,-8],[-8,-8]]
castle_moves = [[0,1],[0,-1],[1,0],[-1,0],[0,2],[0,-2],[2,0],[-2,0],[0,3],[0,-3],[3,0],[-3,0],\
               [0,4],[0,-4],[4,0],[-4,0],[0,5],[0,-5],[5,0],[-5,0],[0,6],[0,-6],[6,0],[-6,0],\
               [0,7],[0,-7],[7,0],[-7,0],[0,8],[0,-8],[8,0],[-8,0]]
queen_moves = [[0,1],[0,-1],[1,0],[-1,0],[0,2],[0,-2],[2,0],[-2,0],[0,3],[0,-3],[3,0],[-3,0],\
               [0,4],[0,-4],[4,0],[-4,0],[0,5],[0,-5],[5,0],[-5,0],[0,6],[0,-6],[6,0],[-6,0],\
               [0,7],[0,-7],[7,0],[-7,0],[0,8],[0,-8],[8,0],[-8,0],[1,1],[-1,1],[1,-1],[-1,-1],\
               [2,2],[-2,2],[2,-2],[-2,-2],[3,3],[-3,3],[3,-3],[-3,-3],[4,4],[-4,4],[4,-4],[-4,-4],\
               [5,5],[-5,5],[5,-5],[-5,-5],[6,6],[-6,6],[6,-6],[-6,-6],[7,7],[-7,7],[7,-7],[-7,-7],\
               [8,8],[-8,8],[8,-8],[-8,-8]]
king_moves = [[1,1],[1,-1],[-1,1],[-1,-1],[0,-1],[0,1],[1,0],[-1,0]]
computer_legit_moves = castle_moves  
human_legit_moves=king_moves

isGoal=False
board_size=[4,8]
human_player_move=[[3,7]]
computer_player_move=[[0,0]]
def checkmate (computer_legit_moves,human_player_move,computer_player_move):
    for i in computer_legit_moves:
        nextmove=[computer_player_move[-1][0]+i[0],computer_player_move[-1][1]+i[1]]
        if nextmove[0]==human_player_move[-1][0] and nextmove[1]==human_player_move[-1][1]:
            print("CHECKMATE")
    
def CPM (board_size, computer_legit_moves,human_player_move):
    global computer_player_move,isGoal
    goal=[human_player_move[0][0],human_player_move[0][1]]
    possible_move=[]
    for i in computer_legit_moves:#生成所有合法路径
            move_position = [computer_player_move[-1][0]+ i[0],computer_player_move[-1][1] + i[1]]#生成一个合法路径
            if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] \
                or move_position[1]>=board_size[1]:#如果超出棋盘外
                continue#继续循环
            else:
                possible_move.append(move_position)
    best_position=possible_move[0]
    for i in possible_move:
        absolute_distance=math.sqrt(abs(goal[0]-best_position[0])**2+abs(goal[1]-best_position[1])**2)
        temp_distance=math.sqrt(abs(goal[0]-i[0])**2+abs(goal[1]-i[1])**2)
        if absolute_distance>temp_distance:
            best_position=i
        else:
            continue
        computer_player_move.append(best_position)
    if best_position==human_player_move[0]:
        isGoal=True
    checkmate(computer_legit_moves, human_player_move, computer_player_move)

def HPM (board_size,legit_moves):
    global human_player_move
    user_input = input('Please input goal position (x, y): ')
    pieces_goal = list(eval(user_input))
    possible_move=[]
    ilegal=True
    for i in legit_moves:#生成所有合法路径
        move_position = [human_player_move[-1][0]+ i[0],human_player_move[-1][1] + i[1]]#生成一个合法路径
        if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] \
            or move_position[1]>=board_size[1]:#如果超出棋盘外
            continue#继续循环
        else:
            possible_move.append(move_position)
    for i in possible_move:
        if i==pieces_goal:
            ilegal=False
    if ilegal:#检查终点输入合法性
        raise TypeError('Goal position break the rule')
    human_player_move.append(pieces_goal)\

def board_print(board_size,human_player_move,computer_player_move):
    board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
    board_display[computer_player_move[-1][0]][computer_player_move[-1][1]] = ' C '
    board_display[human_player_move[-1][0]][human_player_move[-1][1]]  = ' K '
    for i in range(board_size[0]):
        display_string = ''.join(board_display[i])
        print(display_string)   
     
while isGoal==False:
    CPM(board_size,computer_legit_moves,human_player_move)
    board_print(board_size,human_player_move,computer_player_move)
    HPM(board_size,human_legit_moves)
    board_print(board_size,human_player_move,computer_player_move)

print("gameover")