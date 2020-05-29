from collections import deque

def jump(input_deque,step):
    if type(input_deque)!=deque or (type(step)!=int and type(step)!=float):
        return "What did you put in?"
    else:
        for i in range(0,step):
            a=input_deque.popleft()
            input_deque.append(a)
        return input_deque

def in_place_sort(input_deque, reverse):
    if type(input_deque)!=deque or type(reverse)!=bool:
        return "What did you put in?"
    else:
        for i in range(0,len(input_deque)):
            min=float("inf")
            for j in range(i,len(input_deque)):
                temp=input_deque.popleft()
                if min>temp and min!=float("inf"):
                    input_deque.append(min)
                    min=temp
                elif min>temp:
                    min=temp
                else:
                    input_deque.append(temp)
            input_deque.append(min) 
            jump(input_deque,i)
        if reverse==True:
            return input_deque
        elif reverse==False:
            return input_deque.reverse()

input_deque = deque([123,564,645,469,45,123,456,4523,354])
print(in_place_sort(input_deque,False))