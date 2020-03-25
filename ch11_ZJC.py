#第一题
<<<<<<< Updated upstream
def optimal_cut(length):
    """计算不同米数长度的香肠最大能卖多少钱
        length：香肠的米数
        output：卖的最多的钱"""
    price_list = [3,5,8,9,10,17,17,20]
    if length<=0:
        return 0
    if optimal_cut_memory[length] == None:
        max_value = 0
        for cut in range(length):
            max_value = max(max_value, price_list[cut] + optimal_cut(length-cut-1))
        optimal_cut_memory[length] = max_value
    return optimal_cut_memory[length]
price_list = [3,5,8,9,10,17,17,20]
optimal_cut_memory = [None]*(len(price_list) + 1)
result = optimal_cut(len(price_list))
print(result)
#ex1.2

def classify(sentence):
    sentence2 = sentence.lower()
    list_sentence = sentence2.split()
    memory2 = {}
    for n in range(len(list_sentence)):
        if list_sentence[n] in memory2:
            memory2[list_sentence[n]]+= 1
        else:
            memory2[list_sentence[n]] = 1
    return memory2
print(classify('I see you I You You')['you'])
=======
def DP_num(n):
    ''' More efficiently solving fibonacci using a global variable to remember sub-problems
    Parameters:
    - Input: n an integer >=0
    - Output: Integer Fibonacci number
    '''
    times = 1
    if n < 0:
        raise ValueError('Fibonacci argument must be greater than zero.')
    if n > 1:
       if n % 3 == 0:
           times += DP_num(n/3)
       elif n % 2 == 0:
           times += DP_num(n/2)
       else:
           times +=DP_num(n - 1)

    print (times)
    return times

#第二题
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
>>>>>>> Stashed changes
