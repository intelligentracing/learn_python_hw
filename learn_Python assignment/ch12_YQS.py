from collections import deque
import math
#ex1.1
def DFS(board_size, start, goal, legit_moves):
    ''' DFS search a viable path from start position to goal position on the board_size
    Parameters:
    Input:  board_size  - The dimension of the board
            start       - start position of the piece
            goal        - final destination
            legit_moves - describe how the piece can move on the board

    Output: result_path - return a DFS path that reaches the goal, otherwise []
    算法思想：
    我们只需要为代码添加一个筛选路径的条件，即计算当前所选择走的这一步与终点坐标之间的直线距离，
    然后把马可以走的8个步，先通过不可超过边界等条件筛掉一些，
    再对剩下的步法进行这个计算，将计算结果'm'和该点的(x,y)坐标，写成[m,(x,y)]这样的形式，储存到search_stack这个list中，
    search_stack是我们所选择走的步的列表， 对search_stack从大到小排序，然后执行pop操作，
    因为pop是右出，所以计算机就会执行m最小的那个步法的(x,y),达到我们的目的
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
    distance_start = math.sqrt((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2)
    search_stack =[(distance_start,start)] # 将search_stack修改为[(m,(x,y))]的列表形式，start是坐标

    # move_parent records the parent notes of the searched moves on the board
    parent_map = [[[None, None] for i in range(board_size[1])] for j in range(board_size[0])]
    parent_map[start[0]][start[1]] = [-1, -1]
    is_goal = False
    while len(search_stack) > 0 and not is_goal:

        # Retrieve the current FILO position
        current_move = search_stack.pop()#此时current_move是(m,(x,y))形式

        # Generate all legit moves
        for i in legit_moves:

            # Generate a potential move
            move_position = [current_move[1][0] + i[0], current_move[1][1] + i[1]]#所以current_move[1][0]才等于(m,(x,y)中的x

            # This move may be out of bound or have been visited
            if move_position[0] < 0 or move_position[1] < 0 or move_position[0] >= board_size[0] \
                    or move_position[1] >= board_size[1]:
                continue
            elif parent_map[move_position[0]][move_position[1]] != [None, None]:
                continue
            #添加筛选路径的条件
            distance_move = math.sqrt((move_position[0] - goal[0])**2 + (move_position[1] - goal[1])**2)

            # This is a valid position
            parent_map[move_position[0]][move_position[1]] = current_move[1]#这里因为current_move是(m,(x,y))形式，所以current_move[1]才表示(x,y)坐标，
                                                                            # 把它理解为列表中的索引，current_move[0]是m,current_move[1]是(x,y)

            # Check if the new position is the goal
            if move_position == goal:
                is_goal = True
                break
            #给search_stack添加符合条件步法的distance_move和它的坐标即move_position,然后从大到小进行排序
            search_stack.append((distance_move, move_position))
        search_stack.sort(reverse=True)
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

#ex1.2
quotes = ['We can know only that we know nothing. And that is the highest degree of human wisdom.', \
          'Nothing is so necessary for a young man as the company of intelligent women.', \
          'The strongest of all warriors are these two — Time and Patience.', \
          'There is no greatness where there is not simplicity, goodness, and truth.'
          ]

def division_hashing(text):
    """算法思想：
        计算与已知字符串具有相同哈希值的其他字符串，方法：将text中的每一个字符用26个英文字母分别代替，每次只替换一个字符，
        比如，'w'替换成'a',然后计算整个text的hash_value,然后再把'w'换成'b',方法同上，26个字母替换完后，到text的下一个字符'e'，
        进行同上的操作
        text:原来的字符串，格式也为str,字符串格式
        output：有多少相同的字符串，并将它们都打印出来"""
    global hash_prime_number
    hash_prime_number = 101
    letters = 'abcdefghijklmnopqrstuvwxyz'#先给出26个字母的字符串
    text_new = list(text)#将输入的字符串变成list的格式，方便后面替换字符
    text_new_list = []#储存满足条件的字符串
    sum1 = 0
    #将text_new中的字符替换成26个字母中的每一个
    for i in range(len(text_new)):
        b = text_new[i]#先将原来的text_new中被替换的字符赋值出来，在经过下面变换之后，最后要将b,赋值回text_new，\
                       # 否则当前的text_new[i]就会是下面代码中j的最后一个值即'z'
        for j in letters:
            text_new[i] = j
            #计算哈希值,其值为hash_new
            for a in text_new:
                sum1 = sum1 * 256 + ord(a)

            hash_new = sum1 % hash_prime_number

            #判断哈希值是否为原给定字符串的哈希值，原字符串的哈希值为20
            if hash_new == 20:
                text_new_str = ''.join(text_new)#将list形式的text_new变为字符串形式
                text_new_list.append(text_new_str)#将满足条件的字符串添加到储存它的列表中
        text_new[i] = b#将之前赋值出来的b,赋值回去
    num = len(text_new_list)
    print('拥有相同哈希值的字符串共有：', num)
    print('它们分别是：')
    #打印这些符合条件的字符串
    for var in text_new_list:
        print(var)

division_hashing(quotes[0])