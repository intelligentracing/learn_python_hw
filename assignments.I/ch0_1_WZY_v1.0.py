import random
import time
print("please input the range you need.")
Points=eval(input())   
begin_time=time.time()
hits=0.0 
for i in range (0,Points+1):
    x=random.randint(0,Points+1)
    y=random.randint(0,Points+1)
    dist=pow(float(x**2+y**2),0.5)
    if dist<=Points:
        hits+=1
pi=4*(hits/Points)
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(str(pi))
