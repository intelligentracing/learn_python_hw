
def optimal_cut(length):

    if length<=0:
        return 0

    max_value = 0

    for cut in range(0, length):
        max_value = max(max_value, price_list[cut] + optimal_cut(length-cut-1))

    return max_value

price_list = [3,5,8,9,10,17,17,20]

result = optimal_cut(len(price_list))
print(result)