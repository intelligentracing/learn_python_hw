## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: knight_path_DFS.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque

# Assign constant tuples for allowed knight's eight moves
knight_moves = [[-2,-1], [-1,-2], [1,-2],[2,-1], [2,1], [1,2], [-1,2], [-2,1]]

bishop_moves = [[1,1], [2,2], [3,3], [4,4], [-1,-1], [-2,-2], [-3, -3], [-4, -4], \
    [1, -1], [2, -2], [3, -3], [4, -4], [-1,1], [-2,2], [-3,3], [-4,4]]

def DFS(board_size, start, goal, legit_moves, blocks):
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
    parent_map[start[0]][start[1]] = [-1, -1]
    is_goal = False
    while len(search_stack)>0 and not is_goal:
        
        # Retrieve the current FILO position
        current_move = search_stack.pop()

        # Generate all legit moves
        for i in legit_moves:
            
            # Generate a potential move
            move_position = [ current_move[0] + i[0],current_move[1] + i[1]]

            # This move may be out of bound or have been visited
            if move_position[0]<0 or move_position[1]<0 or move_position[0]>=board_size[0] \
                or move_position[1]>=board_size[1]:
                continue
            elif parent_map[move_position[0]][move_position[1]]!=[None, None]:
                continue

            if len(blocks)>0:
                is_blocked = False
                for coordinates in blocks:
                    if move_position==coordinates:
                        is_blocked = True
                        break
                
                if is_blocked:
                    continue

            # This is a valid position
            search_stack.append(move_position)
            parent_map[move_position[0]][move_position[1]] = current_move

            # Check if the new position is the goal
            if move_position == goal:
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
board_size = [4,8]

blocks = [[2, 2], [2,3], [2,4], [2,5], [3,2], [3,3], [3,4], [3,5]]

# Assign knight's initial position
start = [0,0]

# Create a display of the board game problem
print('Game has started, here is the board with the initial position at 0')
board_display = [[' . ' for i in range(board_size[1])] for j in range(board_size[0])]
board_display[start[0]][start[1]] = ' S '
for coordinates in blocks:
    board_display[coordinates[0]][coordinates[1]] = ' X '

for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

# Acquire user input about the goal position
user_input = input('Please input goal position (x, y): ')
goal = list(eval(user_input))

print('Moving Knight from {0} to {1}:'.format(start, goal))
board_display[goal[0]][goal[1]]  = ' G '

search_path = DFS(board_size, start, goal, bishop_moves, blocks)

print(search_path)
if len(search_path)>0:
    start = search_path.popleft()
    search_path.append(start)
    for i in range(1,len(search_path)-1):
        current_move = search_path.popleft()
        board_display[current_move[0]][current_move[1]]  = ' o '
        search_path.append(current_move)
        
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)