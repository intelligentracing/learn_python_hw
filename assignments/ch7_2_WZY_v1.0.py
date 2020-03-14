def C(r,n):
    up=1
    down1=1
    down2=1
    for i in range(1,n+1):
        up=up*i
    for j in range(1,r+1):
        down1=down1*j
    for k in range(1,n-r+1):
        down2=down2*k   
    sum=up/(down1*down2)
    return sum

print("Enter the number of line you need")
line=input()
for l in range(1,int(line)+1):
    list=[]
    for m in range(1,l):
        list.append(int(C(m-1,l-1)))
    list.append(1)
    print(list)
