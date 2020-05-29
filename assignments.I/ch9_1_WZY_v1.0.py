## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: knight_path_DFS.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque
import random

def DFS(board_size, start, goal, legit_moves, current_move):
    ''' DFS search a viable path from start position to goal position on the board_size
    Parameters:
    Input:  board_size  - The dimension of the board
            start       - start position of the piece
            goal        - final destination
            legit_moves - describe how the piece can move on the board
    
    Output: result_path - return a DFS path that reaches the goal, otherwise []
    '''
    # Input sanity check
    if len(board_size)!=2 or type(board_size[0])!=int or type(board_size[1])!=int:
        raise TypeError('Board size is not a compatible type')
    elif board_size[0]<=0 or board_size[1]<=0:
        raise ValueError('Board size value is not supported')

    if len(start)!=2 or type(start[0])!=int or type(start[1])!=int:
        raise TypeError('Start position is not a compatible type')
    elif start[0]<0 or start[1]<0 or start[0]>=board_size[0] or start[1]>=board_size[1]:
        raise ValueError('Start position value is not supported')

    if len(goal)!=2 or type(goal[0])!=int or type(goal[1])!=int:
        raise TypeError('Goal position is not a compatible type')
    elif goal[0]<0 or goal[1]<0 or goal[0]>=board_size[0] or goal[1]>=board_size[1]:
        raise ValueError('Start position value is not supported')

    # Initialization
    search_stack = deque()    # this is a queue to manage the order of the DFS
    search_stack.append(start)

    # move_parent records the parent notes of the searched moves on the board
    parent_map  = [[[None,None] for i in range(board_size[1])] for j in range(board_size[0])]
    is_goal = False
    
    while len(search_stack)>0 and not is_goal:
        
        # Retrieve the current FIFO position
        previous_move = current_move
        current_move = search_stack.pop()
        parent_map[current_move[0]][current_move[1]] = previous_move

        # Generate all legit moves
        for i in legit_moves:
            
            # Generate a potential move
            move_position = [ current_move[0] + i[0],current_move[1] + i[1]]

            # This move may be out of bound or have been visited
            if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] \
                or move_position[1]>=board_size[1] or (move_position[0]==2 and move_position[1]==2) or \
                    (move_position[0]==2 and move_position[1]==3) or \
                    (move_position[0]==2 and move_position[1]==4) or \
                    (move_position[0]==2 and move_position[1]==5) or \
                    (move_position[0]==3 and move_position[1]==2) or \
                    (move_position[0]==3 and move_position[1]==3) or \
                    (move_position[0]==3 and move_position[1]==4) or \
                    (move_position[0]==3 and move_position[1]==5):
                continue
            elif parent_map[move_position[0]][move_position[1]]!=[None, None]:
                continue

            # This is a valid position
            search_stack.append(move_position)

            # Check if the new position is the goal
            if move_position == goal:
                parent_map[move_position[0]][move_position[1]] = current_move
                is_goal = True
                break
        
    path_queue = deque()
    if is_goal:
        # Assign the found path and quit
        while is_goal:
            path_queue.appendleft(move_position)
            move_position = parent_map[move_position[0]][move_position[1]]
            if move_position[0]==-1:
                is_goal = False
            
    return path_queue


# Assign chess board size. Here half a standard board is used
board_size = [8,8]
current_move = [-1, -1]

# Assign constant tuples for allowed knight's eight moves
knight_moves = [[-2,-1], [-1,-2], [1,-2],[2,-1], [2,1], [1,2], [-1,2], [-2,1]]
bishop_moves = [[1,1],[-1,1],[1,-1],[-1,-1],\
               [2,2],[-2,2],[2,-2],[-2,-2],\
               [3,3],[-3,3],[3,-3],[-3,-3],\
               [4,4],[-4,4],[4,-4],[-4,-4],\
               [5,5],[-5,5],[5,-5],[-5,-5],\
               [6,6],[-6,6],[6,-6],[-6,-6],\
               [7,7],[-7,7],[7,-7],[-7,-7],\
               [8,8],[-8,8],[8,-8],[-8,-8],]
pieces_moves = bishop_moves          

# Assign knight's initial position
pieces_start = [0,0]

# Create a display of the board game problem
print('Game has started, here is the board with the initial position at 0')
board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
board_display[pieces_start[0]][pieces_start[1]] = ' S '
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

# Acquire user input about the goal position
user_input = input('Please input goal position (x, y): ')
pieces_goal = list(eval(user_input))

print('Moving Pieces from {0} to {1}:'.format(pieces_start, pieces_goal))
board_display[pieces_goal[0]][pieces_goal[1]]  = ' G '

pieces_path = DFS(board_size, pieces_start, pieces_goal, pieces_moves, current_move)

print(pieces_path)
if len(pieces_path)>0:
    start = pieces_path.popleft()
    pieces_path.append(start)
    for i in range(1,len(pieces_path)-1):
        current_move = pieces_path.popleft()
        board_display[current_move[0]][current_move[1]]  = ' o '
        pieces_path.append(current_move)
        
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)