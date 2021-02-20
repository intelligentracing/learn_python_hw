#ex1.1
def DP_num(num):
    if num == 1:
        return 0
    elif num <= 3:
        return 1
    
    dp_list = [0]*num
    dp_list[0] = 0
    dp_list[1] = 1
    dp_list[2] = 1
    for i in range(3, len(dp_list) + 1):
        #相当于第一种情况i - 1
        minn = [dp_list[i - 1]]
        if i%2 == 0:
            minn.append(dp_list[i//2])
        if i%3 == 0:
            minn.append(dp_list[i // 3])
        #从这三步里找出步数最少的那个 + 1就是这个数字到1的最少步数
        dp_list[i] = min(minn) + 1
        
    return dp_list[-1]

print(DP_num(675))

#ex1.2
price = [3,5,8,9,10,17,17,20]
n = 8

def solution(price, n):
    """Apply subproblem optimality to solve the problem of how best to cut
        price：It's a list of prices sold for different meters
        n:It's an int, how many meters are there in this sausage
    """
    dp = [0] * n    #subproblem optimal solution
    for i in range(n):      #start at 1 meter, and calculate the highest selling price
        dp[i] = price[i]    #The price when i meters are sold as a whole
        for j in range(i):  
            #When i meters are sold separately。The key: Turn a big problem into a small problem, 
            #and the optimal solution to the small problem is also the optimal solution to the big problem
            if dp[i - j-1] + dp[j] > dp[i]: #Compare that to selling as a whole
                dp[i] = dp[i-j-1] + dp[j]
    return dp[-1]

print(solution(price,n))
