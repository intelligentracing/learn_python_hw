#第一题
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