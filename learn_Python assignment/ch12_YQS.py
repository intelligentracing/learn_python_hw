from collections import deque
import math

#ex1.1
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
            #'We can" ->  text_new = 'we can'
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
