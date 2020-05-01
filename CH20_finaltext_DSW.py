#
#
#
#
#
#
#
#第8题
import math 
# Assign chess board size. Here half a standard board is used
board_size = [4,8]

# Assign constant tuples for allowed knight's eight moves
knight_moves = [[1,2], [1,-2], [-1,2],[-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]

# Assign knight's initial position
knight_start = [3,7]
king_start =[0,0]

# Create a display of the board game problem
print('Game has started, here is the board with the initial position at 0')
board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
board_display[knight_start[0]][knight_start[1]] = ' S '
board_display[king_start[0]][king_start[1]] = 'G'
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

def DFS(board_size, start, start1, legit_moves):
    ''' DFS search a viable path from start position to goal position on the board_size
    Parameters:
    Input:  board_size  - The dimension of the board
            start       - start position of the piece
            goal        - final destination
            legit_moves - describe how the piece can move on the board
    Output: result_path - return a DFS path that reaches the goal, otherwise []
    '''
    # Input sanity check
    if len(board_size) != 2 or type(board_size[0]) != int or type(board_size[1]) != int:
        raise TypeError('Board size is not a compatible type')
    elif board_size[0] <= 0 or board_size[1] <= 0:
        raise ValueError('Board size value is not supported')

    if len(start) != 2 or type(start[0]) != int or type(start[1]) != int:
        raise TypeError('Start position is not a compatible type')
    elif start[0] < 0 or start[1] < 0 or start[0] >= board_size[0] or start[1] >= board_size[1]:
        raise ValueError('Start position value is not supported')

    if len(start1) != 2 or type(start1[0]) != int or type(start1[1]) != int:
        raise TypeError('Goal position is not a compatible type')
    elif start1[0] < 0 or start1[1] < 0 or start1[0] >= board_size[0] or start1[1] >= board_size[1]:
        raise ValueError('Start position value is not supported')

    # Initialization
    distance_start = math.sqrt((start[0] - start1[0]) ** 2 + (start[1] - start1[1]) ** 2)
    search_stack = [(distance_start, start, start1)]  # 将search_stack修改为[(m,(x,y))]的列表形式，start是坐标

    # move_parent records the parent notes of the searched moves on the board
    parent_map = [[[None, None] for i in range(board_size[1])] for j in range(board_size[0])]
    parent_map[start[0]][start[1]] = [-1, -1]
    is_goal = False
    current_move = [0,(0,0),(3,7)]
    while len(search_stack) > 0 and not is_goal:
        user_input = input("Please input next step position for king(x,y): ")
        move_position = list(eval(user_input))
        # Retrieve the current FILO position

        # Generate all legit moves
        for i in legit_moves:

            # Generate a potential move
            move_position1 = [current_move[2][0] + i[0], current_move[2][1] + i[1]]  # 所以current_move[1][0]才等于(m,(x,y)中的x

            # This move may be out of bound or have been visited
            if move_position[0] < 0 or move_position[1] < 0 or move_position[0] >= board_size[0] \
                    or move_position[1] >= board_size[1] or move_position1[0] < 0 or move_position1[1] < 0 \
                    or move_position1[0] >= board_size[0] or move_position1[1] >= board_size[1]:
                continue
            elif (move_position[0] == move_position1[0] and abs(move_position[1] -move_position1[1]) == 1) or  (move_position[1] == move_position1[1] \
                    and abs(move_position[0]- move_position1[0]) == 1):
                continue
            elif parent_map[move_position1[0]][move_position1[1]] != [None, None]:
                continue
            # 添加筛选路径的条件
            distance_move = math.sqrt((move_position[0] - move_position1[0]) ** 2 + (move_position[1] - move_position1[1]) ** 2)

            # This is a valid position
            parent_map[move_position[0]][move_position[1]] = current_move[2]  # 这里因为current_move是(m,(x,y))形式，所以current_move[1]才表示(x,y)坐标，
            # 把它理解为列表中的索引，current_move[0]是m,current_move[1]是(x,y)

            # Check if the new position is the goal
            if move_position == move_position1:
                is_goal = True
                print('knight position:',move_position1,'King positon',move_position,'Knight win!!!!')
                board_display[move_position[0]][move_position[1]] = ' ⊕ '
                board_display[current_move[2][0]][current_move[2][1]] = ' o '
                for i in range(board_size[0]):
                    display_string = ''.join(board_display[i])
                    print(display_string)
                return
            # 给search_stack添加符合条件步法的distance_move和它的坐标即move_position,然后从大到小进行排序
            search_stack.append((distance_move, move_position, move_position1))
        search_stack.sort(reverse=True)
        current_move = search_stack.pop()
        board_display[move_position[0]][move_position[1]] = ' + '
        board_display[current_move[2][0]][current_move[2][1]] = ' o '
        for i in range(board_size[0]):
            display_string = ''.join(board_display[i])
            print(display_string)

DFS(board_size, king_start,knight_start, knight_moves)

