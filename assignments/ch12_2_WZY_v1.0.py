## This is course material for Introduction to Python Scientific Programming
## Class 12 Example code: hash_search.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

quotes = ['We can know only that we know nothing. And that is the highest degree of human wisdom.',\
        'Nothing is so necessary for a young man as the company of intelligent women.',\
        'The strongest of all warriors are these two — Time and Patience.',\
        'There is no greatness where there is not simplicity, goodness, and truth.'
        ]

def division_hashing(text):
    global hash_prime_number
    hash_prime_number = 101

    sum = 0
    for c in text:
        sum = sum*256 + ord(c)  # Change a character to its ASCII value
    
    return sum % hash_prime_number

def find_hash(text):
    find_hash=False
    hash_number=division_hashing(text)
    haha=text
    while find_hash is not True:
        haha=list(haha)
        for c in range(len(haha)):
            for i in range(32,128):
                del haha[c]
                haha.insert(c,chr(i))
                haha="".join(haha)
                temp_hash=division_hashing(haha)
                if temp_hash==hash_number and haha!=text:
                    find_hash=True
                    return haha
                    break
                else:
                    haha=list(haha)

print(quotes[0])
print(find_hash(quotes[0]))