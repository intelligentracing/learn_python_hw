#Midium2 ex2_Global_variables.py
#Author: Yu Qiuhsuang

from queue import deque
encryption = 2

def encode(string):
    user_input = deque(string)
    for i in range(len(user_input)):
        original = user_input.popleft()
        #ord()function to convert a single character string to its corresponding ASCII code
        #chr() function to convert the ASCII code back to a single character.
        result = chr(ord(original) + encryption)
        user_input.append(result)
    user_input = ''.join(user_input)
    return user_input

def decode(string):
    user_input = deque(string)
    for i in range(len(user_input)):
        original = user_input.popleft()
        result = chr(ord(original) - encryption)
        user_input.append(result)
    user_input = ''.join(user_input)
    return user_input

print(encode('Rachel'))
print(decode('Tcejgn'))