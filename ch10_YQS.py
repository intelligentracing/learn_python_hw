#ex1.1
def DP_num(n，flag = 1):
    ''' More efficiently solving  less steps into 1
    Parameters:
    - Input: n an integer >=0, flag:insure n first time into function times == 1
    - Output: number of steps
    '''
     if flag == 1:
        times = 1
    else:
        times = 0
    if n < 0:
        raise ValueError('argument must be greater than zero.')
    if n > 1:
       if n % 3 == 0:
           times += DP_num(n/3)
       elif n % 2 == 0:
           times += DP_num(n/2)
       else:
           times +=DP_num(n - 1)

    print (times)
    return times
flag = 0
print(DP_num(10,flag))
#ex1.2
price = [3,5,8,9,10,17,17,20]
n = 8

def solution(price, n):
    """应用子问题最优性来解怎么切最合适问题
        price：是一个list,里面存放着不同米数所卖的价格
        n:是一个int,表示这跟肠有多少m"""
    dp = [0] * n
    jm= 0
    js = 0
    #dp[0] = price[0]
    for i in range(n):      #从1m开始，计算卖最高的价格
        dp[i] = price[i]    #当i米整体卖时的价格
        for j in range(i):  #当i米分开卖时价格，分成两截，切都卖最优价格。关键：将大问题转换成小问题，且小问题的最优解也是大问题的最优解。
            if dp[i - j-1] + dp[j] > dp[i]: #与整体卖比较
                dp[i] = dp[i-j-1] + dp[j]
                jm= j+1
                js = i-j
        print('有',i+1,'米时','切在',jm,'米','剩余 ',js,'米')
    return dp

print(solution(price,n))
