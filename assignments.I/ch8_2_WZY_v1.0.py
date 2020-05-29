from collections import deque
   
def in_place_sort(input_deque, reverse):
    if type(input_deque)!=deque or type(reverse)!=bool:
        return "What did you put in?"
    else: 
        sorted_deque=deque()
        for i in range(0,len(input_deque)):
            min=float("inf")
            for j in range(0,len(input_deque)):
                temp=input_deque.popleft()
                if min>temp:
                    input_deque.append(min)
                    min=temp
                else:
                    input_deque.append(temp)
            sorted_deque.append(min) 
        if reverse==False:
            return sorted_deque
        elif reverse==True:
            return sorted_deque.reverse()

input_deque = deque([123,564,645,469,45,123,456,4523,354])
print(in_place_sort(input_deque,False))