from collections import deque
def input_sort(input_deque, reverse):
    if type(input_deque)!=deque or type(reverse)!=bool:
        return "What did you put in?"
    else:
        for i in range(0,len(input_deque)):
            a=input_deque.popleft()
            aIsSmaller=False
            times=0
            while (aIsSmaller==False):
                b=input_deque.popleft()
                if a<b or times>len(input_deque):
                    aIsSmaller==True
                    input_deque.append(a)
                times+=1
                input_deque.append(b)
        return input_deque
input_deque = deque([123,564,645,469,45,123,456,4523,354])
print(input_sort(input_deque,False))