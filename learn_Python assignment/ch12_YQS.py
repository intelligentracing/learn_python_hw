from collections import deque
import math
#ex1.1
# def DFS(board_size, start, goal, legit_moves):
#     ''' DFS search a viable path from start position to goal position on the board_size
#     Parameters:
#     Input:  board_size  - The dimension of the board
#             start       - start position of the piece
#             goal        - final destination
#             legit_moves - describe how the piece can move on the board

#     Output: result_path - return a DFS path that reaches the goal, otherwise []
#     算法思想：
#     我们只需要为代码添加一个筛选路径的条件，即计算当前所选择走的这一步与终点坐标之间的直线距离，
#     然后把马可以走的8个步，先通过不可超过边界等条件筛掉一些，
#     再对剩下的步法进行这个计算，将计算结果'm'和该点的(x,y)坐标，写成[m,(x,y)]这样的形式，储存到search_stack这个list中，
#     search_stack是我们所选择走的步的列表， 对search_stack从大到小排序，然后执行pop操作，
#     因为pop是右出，所以计算机就会执行m最小的那个步法的(x,y),达到我们的目的
#     '''
#     # Input sanity check
#     if len(board_size) != 2 or type(board_size[0]) != int or type(board_size[1]) != int:
#         raise TypeError('Board size is not a compatible type')
#     elif board_size[0] <= 0 or board_size[1] <= 0:
#         raise ValueError('Board size value is not supported')

#     if len(start) != 2 or type(start[0]) != int or type(start[1]) != int:
#         raise TypeError('Start position is not a compatible type')
#     elif start[0] < 0 or start[1] < 0 or start[0] >= board_size[0] or start[1] >= board_size[1]:
#         raise ValueError('Start position value is not supported')

#     if len(goal) != 2 or type(goal[0]) != int or type(goal[1]) != int:
#         raise TypeError('Goal position is not a compatible type')
#     elif goal[0] < 0 or goal[1] < 0 or goal[0] >= board_size[0] or goal[1] >= board_size[1]:
#         raise ValueError('Start position value is not supported')

#     # Initialization
#     distance_start = math.sqrt((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2)
#     search_stack =[(distance_start,start)] # 将search_stack修改为[(m,(x,y))]的列表形式，start是坐标

#     # move_parent records the parent notes of the searched moves on the board
#     parent_map = [[[None, None] for i in range(board_size[1])] for j in range(board_size[0])]
#     parent_map[start[0]][start[1]] = [-1, -1]
#     is_goal = False
#     while len(search_stack) > 0 and not is_goal:

#         # Retrieve the current FILO position
#         current_move = search_stack.pop()#此时current_move是(m,(x,y))形式

#         # Generate all legit moves
#         for i in legit_moves:

#             # Generate a potential move
#             move_position = [current_move[1][0] + i[0], current_move[1][1] + i[1]]#所以current_move[1][0]才等于(m,(x,y)中的x

#             # This move may be out of bound or have been visited
#             if move_position[0] < 0 or move_position[1] < 0 or move_position[0] >= board_size[0] \
#                     or move_position[1] >= board_size[1]:
#                 continue
#             elif parent_map[move_position[0]][move_position[1]] != [None, None]:
#                 continue
#             #添加筛选路径的条件
#             distance_move = math.sqrt((move_position[0] - goal[0])**2 + (move_position[1] - goal[1])**2)

#             # This is a valid position
#             parent_map[move_position[0]][move_position[1]] = current_move[1]#这里因为current_move是(m,(x,y))形式，所以current_move[1]才表示(x,y)坐标，
#                                                                             # 把它理解为列表中的索引，current_move[0]是m,current_move[1]是(x,y)

#             # Check if the new position is the goal
#             if move_position == goal:
#                 is_goal = True
#                 break
#             #给search_stack添加符合条件步法的distance_move和它的坐标即move_position,然后从大到小进行排序
#             search_stack.append((distance_move, move_position))
#         search_stack.sort(reverse=True)
#     path_queue = deque()
#     if is_goal:
#         # Assign the found path and quit
#         while is_goal:
#             path_queue.appendleft(move_position)
#             move_position = parent_map[move_position[0]][move_position[1]]
#             if move_position[0] == -1:
#                 is_goal = False

#     return path_queue


# # Assign chess board size. Here half a standard board is used
# board_size = [4, 8]

# # Assign constant tuples for allowed knight's eight moves
# knight_moves = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

# # Assign knight's initial position
# knight_start = [0, 0]

# # Create a display of the board game problem
# print('Game has started, here is the board with the initial position at 0')
# board_display = [[' * ' for i in range(board_size[1])] for j in range(board_size[0])]
# board_display[knight_start[0]][knight_start[1]] = ' S '
# for i in range(board_size[0]):
#     display_string = ''.join(board_display[i])
#     print(display_string)

# # Acquire user input about the goal position
# user_input = input('Please input goal position (x, y): ')
# knight_goal = list(eval(user_input))

# print('Moving Knight from {0} to {1}:'.format(knight_start, knight_goal))
# board_display[knight_goal[0]][knight_goal[1]] = ' G '

# knight_path = DFS(board_size, knight_start, knight_goal, knight_moves)

# print(knight_path)
# if len(knight_path) > 0:
#     start = knight_path.popleft()
#     knight_path.append(start)
#     for i in range(1, len(knight_path) - 1):
#         current_move = knight_path.popleft()
#         board_display[current_move[0]][current_move[1]] = ' o '
#         knight_path.append(current_move)

# for i in range(board_size[0]):
#     display_string = ''.join(board_display[i])
#     print(display_string)

#ex1.2
quotes = ['We can know only that we know nothing. And that is the highest degree of human wisdom.', \
          'Nothing is so necessary for a young man as the company of intelligent women.', \
          'The strongest of all warriors are these two — Time and Patience.', \
          'There is no greatness where there is not simplicity, goodness, and truth.'
          ]

def division_hashing(text):
    """idea of the algorithm：
        Evaluates other strings that have the same hash value as a known string，method：Replace each character in the text with 26 English letters, one character at a time.
        eg，Replace 'w' with 'a',Then calculate the hash_value for the entire text,Then, replace 'w' with 'b', same as above. After the 26 letters are replaced, 
        go to the next character 'e' of the text and do the same
        text:input string 
        output：How many identical strings and print them all out
    """
    global hash_prime_number
    hash_prime_number = 101
    sum1 = 0
    
    #initialization
    letters = 'abcdefghijklmnopqrstuvwxyz'#start with a 26-letter string
    text_new = list(text)#Change the input string into a list format to make it easier to replace characters later
    text_new_list = []#Stores strings that meet the criteria
    

    #Replace the characters in text_new with each of the 26 letters
    for i in range(len(text_new)):
        b = text_new[i]#Assign the character that was replaced in the original text_new, and after the following transformation, assign b back to text_new，\
                       # Otherwise the current text_new[I] will be the last value of j in the following code which is 'z'
        for j in letters:
            text_new[i] = j
            #Evaluates the hash value, which is hash_new
            for a in text_new:
                sum1 = sum1 * 256 + ord(a)

            hash_new = sum1 % hash_prime_number

            #Determines whether the hash value is the original hash value of the given string,original value is 20
            if hash_new == 20:
                text_new_str = ''.join(text_new)#Change text_new as a list to a string
                text_new_list.append(text_new_str)#Adds the conditional string to the list in which it is stored
        text_new[i] = b# assign b back to input text
    num = len(text_new_list)
    print('拥有相同哈希值的字符串共有：', num)
    print('它们分别是：')
    #Print these qualifying strings
    for var in text_new_list:
        print(var)

division_hashing(quotes[0])