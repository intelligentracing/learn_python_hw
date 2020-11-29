# from ch13_YQS import Square

# s1 = Square(8)
# s2 = Square(8)

# enroll = s1 + s2
# print(s1.get_area())
# print(enroll.get_area())

def appendTail(orign, value):
    orign.append(value)
    return orign

def deleteHead(orign, value):
    stack = []
    while orign:
        stack.append(orign.pop())
    stack.pop()
    while stack:
        orign.append(stack.pop())
    
    return orign