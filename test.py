def optimal_cut(length):
    """计算不同米数长度的香肠最大能卖多少钱
        length：香肠的米数
        output：卖的最多的钱"""

    if length<=0:
        return 0
    if optimal_cut_memory[length] == None:
        max_value = 0
        for cut in range(length):
            max_value = max(max_value, price_list[cut] + optimal_cut(length-cut-1))
        optimal_cut_memory[length] = max_value
    return optimal_cut_memory[length]

price_list = [3,5,8,9,10,17,17,20]
#optimal_cut_memory是为了储存所有米数的最优解所设的list,因为列表的第一位索引为[0]，但是输入的length最小为1，所以list应该比len(length)大1
#optimal_cut_memory的第一位将一直为None，因为一直不会调用它
optimal_cut_memory = [None]*(len(price_list) + 1)

result = optimal_cut()
print(result)