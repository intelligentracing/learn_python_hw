
def how_many_lunar_years(start_year,end_year):
    try:
        if start_year<0 or end_year<0 or end_year<start_year:
            print("输入正确的年份")
        else:
            x = start_year
            y = end_year
            print("从{0}到{0}有：".format(x,y),end ="")
            while True:
                if x == y+1 :
                    break
                if x%4 == 0:
                    print(x,end =",")
                    x+=1
                else:
                    x+=1
            print("为闰年")
    except:
        print("错误")

def random_number_in_order():
    import random
    A = random.randint(0,100)
    B = random.randint(0,100)
    C = random.randint(0,100)
    D = random.randint(0,100)
    E = random.randint(0,100)
    F = random.randint(0,100)
    G = random.randint(0,100)
    H = random.randint(0,100)
    Y = random.randint(0,100)
    J = random.randint(0,100)
    K = random.randint(0,100)
    List = [A,B,C,D,E,F,G,H,Y,J,K]
    print(sorted(List))

random_number_in_order()

how_many_lunar_years(2020,2040)

    
    

        



