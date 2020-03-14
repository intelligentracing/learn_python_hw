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
    for n in range(0,int(line)-l):
        print(" ",end="")
    for m in range(1,l):
        print(int(C(m-1,l-1)),end=""),
        print(" ",end="")
    print(1)