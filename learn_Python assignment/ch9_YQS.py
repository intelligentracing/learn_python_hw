from collections import deque

ex1.1
def merge_sort(input_list,reverse = False):
    ''' Merge sort function using recursion
    Parameters:
    Input:  input_list  - a list of numerical numbers

    Output: input_list  - sorted list
    '''

    # Deploy Divide-and-Conquer
    if type(reverse)!=bool and type(input_list) != list:
        return False
    if reverse == False:
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left_half = input_list[:mid]
            right_half = input_list[mid:]

            # Recursively sort left and right sub-lists
            merge_sort(left_half)
            merge_sort(right_half)

            # Merging left_half and right_half
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    input_list[k] = left_half[i]
                    i = i + 1
                else:
                    input_list[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                input_list[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                input_list[k] = right_half[j]
                j = j + 1
                k = k + 1
    elif reverse == True:
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left_half = input_list[:mid]
            right_half = input_list[mid:]

            # Recursively sort left and right sub-lists
            merge_sort(left_half,reverse=True)
            merge_sort(right_half,reverse=True)

            # Merging left_half and right_half
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] >= right_half[j]:
                    input_list[k] = left_half[i]
                    i = i + 1
                else:
                    input_list[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                input_list[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                input_list[k] = right_half[j]
                j = j + 1
                k = k + 1

sample_count = 20
random_input = random.sample(range(0, sample_count),sample_count)

# ******** Method: Merge Sort ********
print('*** Merge Sort ***')
list1 = [1,3,2,4]
#list1 = random_input.copy()
merge_sort(list1,reverse=True)
print(list1)

#ex1.2
def find_flag(opt_queue,num):
    """找到num在已经排好序的opt_queue里应该放在什么位置，即flag"""
    index = 0
    for i in range(len(opt_queue)):
        com = opt_queue.popleft()
        if com < num:
            index = i+1 #flag代表比几个数小 有flag数比较大
        opt_queue.append(com)
    return index

def insert(opt_queue,index,num):
    """把num插入opt_queue中"""
    new_queue=deque()
    for i in range(index):
        new_queue.append(opt_queue.popleft())    
    new_queue.append(num)
    for i in range(len(opt_queue)):
        new_queue.append(opt_queue.popleft())
    
    return new_queue

def sort_function(queue):
    """循环以上操作将未排序的queue中的每一个元素插入到在opt_queue这个已经排好序的列表中"""
    opt_queue = deque()

    for i in range(len(queue)):
        num = queue.popleft()
        index = find_flag(opt_queue,num)
        opt_queue = insert(opt_queue, index, num)
    return opt_queue

queue_1 = deque([2,10,1])
print(sort_function(queue_1))

#ex1.3
def DFS(board_size, start, goal, legit_moves):
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

    if len(goal) != 2 or type(goal[0]) != int or type(goal[1]) != int:
        raise TypeError('Goal position is not a compatible type')
    elif goal[0] < 0 or goal[1] < 0 or goal[0] >= board_size[0] or goal[1] >= board_size[1]:
        raise ValueError('Start position value is not supported')

    # Initialization
    search_stack = deque()  # this is a queue to manage the order of the DFS
    search_stack.append(start)

    # move_parent records the parent notes of the searched moves on the board
    parent_map = [[[None, None] for i in range(board_size[1])] for j in range(board_size[0])]
    parent_map[start[0]][start[1]] = [-1, -1]
    is_goal = False
    while len(search_stack) > 0 and not is_goal:

        # Retrieve the current FILO position
        current_move = search_stack.pop()

        # Generate all legit moves
        for i in legit_moves:

            # Generate a potential move
            move_position = [current_move[0] + i[0], current_move[1] + i[1]]

            # This move may be out of bound or have been visited
            if move_position[0] < 0 or move_position[1] < 0 or move_position[0] >= board_size[0] \
                    or move_position[1] >= board_size[1]:
                continue
            if move_position[0] > 1 and move_position[1] >1 and move_position[1] <=5:
                continue
            elif parent_map[move_position[0]][move_position[1]] != [None, None]:
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
            if move_position[0] == -1:
                is_goal = False

    return path_queue


# Assign chess board size. Here half a standard board is used
board_size = [4, 8]

# Assign constant tuples for allowed knight's eight moves
knight_moves = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

# Assign knight's initial position
knight_start = [0, 0]

# Create a display of the board game problem
print('Game has started, here is the board with the initial position at 0')
board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
board_display[knight_start[0]][knight_start[1]] = ' S '
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

# Acquire user input about the goal position
user_input = input('Please input goal position (x, y): ')
knight_goal = list(eval(user_input))

print('Moving Knight from {0} to {1}:'.format(knight_start, knight_goal))
board_display[knight_goal[0]][knight_goal[1]] = ' G '

knight_path = DFS(board_size, knight_start, knight_goal, knight_moves)

print(knight_path)
if len(knight_path) > 0:
    start = knight_path.popleft()
    knight_path.append(start)
    for i in range(1, len(knight_path) - 1):
        current_move = knight_path.popleft()
        board_display[current_move[0]][current_move[1]] = ' o '
        knight_path.append(current_move)

for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)


