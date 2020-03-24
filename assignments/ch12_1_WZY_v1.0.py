#ex1.2
price = [3,5,8,9,10,17,17,20]
n = 8

def solution(price, n):
    dp = [0] * n
    jm= 0
    js = 0
    #dp[0] = price[0]
    for i in range(n):     
        dp[i] = price[i]  
        for j in range(i): 
            if dp[i - j-1] + dp[j] > dp[i]: 
                dp[i] = dp[i-j-1] + dp[j]
                jm= j+1
                js = i-j
        print('有',i+1,'米时','切在',jm,'米','剩余 ',js,'米')
    return dp

print(solution(price,n))