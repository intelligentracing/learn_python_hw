def triangle(List,n=15):#n=行数
    if len(List)<=n:
        List1=List.copy()
        List=[]
        if List1!=[]:
            List.append(1)
            for x in range(0,len(List1)-1):
                List.append(List1[x]+List1[x+1])
            List.append(1)
            for n in range(0,n-len(List1)+25):
                print(" ",end="")
            print(List)
        else:
            List = List1 =[1]
            for x in range(0,n-len(List1)+25):
                print(" ",end="")
            print(List)
        triangle(List)
triangle([],20)#20=间隔数量