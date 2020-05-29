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

##
from collections import deque
import random
import math

#所有棋子的移动方式
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

#确认棋子合法路径
computer_legit_moves = knight_moves  
human_legit_moves=king_moves

#确定基本参数
isGoal=False
board_size=[4,8]

#人类玩家路径与电脑玩家路径
human_player_move=[[3,7]]
computer_player_move=[[0,0]]

#检查checkmate
def checkmate (computer_legit_moves,human_player_move,computer_player_move):
    #循环电脑可能路径
    for i in computer_legit_moves:
        nextmove=[computer_player_move[-1][0]+i[0],computer_player_move[-1][1]+i[1]]
        #如果电脑的下一步路径与人类玩家位置重合
        if nextmove[0]==human_player_move[-1][0] and nextmove[1]==human_player_move[-1][1]:
            #checkmte
            print("CHECKMATE")

#电脑下棋  
def CPM (board_size, computer_legit_moves,human_player_move):
    #引用全局变量:电脑路径,目标位置
    global computer_player_move,isGoal
    #目标位置设定为人类玩家的最后位置
    goal=[human_player_move[-1][0],human_player_move[-1][1]]
    #可能的移动路径
    possible_move=[]
    #生成所有合法路径
    for i in computer_legit_moves:
            #生成一个合法路径
            move_position = [computer_player_move[-1][0]+ i[0],computer_player_move[-1][1] + i[1]]
            #若合法路径不在棋盘内
            if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] or move_position[1]>=board_size[1]:#如果超出棋盘外
                continue
            else:
                #将合法路径添加到可能路径中
                possible_move.append(move_position)
    #计算最佳路径
    best_position=possible_move[0]
    #计算所有最优路径
    for i in possible_move:
        #比较可能路径与最优路径相对于目标位置的绝对距离
        absolute_distance=math.sqrt(abs(goal[0]-best_position[0])**2+abs(goal[1]-best_position[1])**2)
        temp_distance=math.sqrt(abs(goal[0]-i[0])**2+abs(goal[1]-i[1])**2)
        #比较可能路径与可能最优路径
        if absolute_distance>temp_distance:
            best_position=i
        else:
            continue
        #将最优路径添加到棋盘
        computer_player_move.append(best_position)
    #若最优路径是棋子当前位置
    if best_position==human_player_move[-1]:
        #游戏结束
        isGoal=True
    #检查checkmate
    checkmate(computer_legit_moves, human_player_move, computer_player_move)

#人类玩家下棋
def HPM (board_size,legit_moves):
    #引用全局变量人类玩家移动步骤
    global human_player_move
    #收取用户输入
    user_input = input('Please input goal position (x, y): ')
    pieces_goal = list(eval(user_input))
    #假设用户输入路径非法
    ilegal=True
    #生成所有合法路径
    for i in legit_moves:
        #生成一个合法路径
        move_position = [human_player_move[-1][0]+ i[0],human_player_move[-1][1] + i[1]]
        #如果超出棋盘外
        if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] \
            or move_position[1]>=board_size[1]:
            continue
        else:
            #如果该合法路径与用户输入相同
            if move_position==pieces_goal:
                #用户输入合法
                ilegal=False
                break
    if ilegal:#检查终点输入合法性
        raise TypeError('Goal position break the rule')
    #将输入添加到棋盘
    human_player_move.append(pieces_goal)

#打印棋盘
def board_print(board_size,human_player_move,computer_player_move):
    #生成空棋盘
    board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
    #将人类玩家与电脑玩家路径填充
    board_display[computer_player_move[-1][0]][computer_player_move[-1][1]] = ' C '
    board_display[human_player_move[-1][0]][human_player_move[-1][1]]  = ' K '
    #打印棋盘
    for i in range(board_size[0]):
        display_string = ''.join(board_display[i])
        print(display_string)   
     
#在游戏结束前
while isGoal==False:
    #打印棋盘
    board_print(board_size,human_player_move,computer_player_move)
    #人类玩家移动
    HPM(board_size,human_legit_moves)
    #打印棋盘
    board_print(board_size,human_player_move,computer_player_move)
    #电脑玩家移动
    CPM(board_size,computer_legit_moves,human_player_move)
    #分界线
    print("---------------------------------------")
#打印游戏结束
print("gameover")