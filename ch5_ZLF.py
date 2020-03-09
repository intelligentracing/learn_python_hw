
def how_many_lunar_years():
    start_year = int(input("输入起始年"))
    end_year = int(input("输入结束年"))
    try:
        if start_year<0 or end_year<0 or end_year<start_year:
            print("输入正确的年份")
        else:
            x = start_year
            y = end_year
            print("从{0}到{1}有：".format(x,y),end ="")
            for n in range(x,y+1):
                if n%4 == 0 and n%100 != 0:
                    print(n,end =",")
                elif n%400 == 0:
                    print(n,end=",")

            print("为闰年")
    except:
        print("错误")

def random_number_in_order():
    import random
    
    List = []
    List2= []
    for Z in range(0,11):
        List.append(random.randint(0,100))
    for D in range(0,100):
        for Z in range(0,11):
            if List[Z] == D:
                List2.append(List[Z])
    print(List2)
                
            
        


    
random_number_in_order()

how_many_lunar_years()

    

        



