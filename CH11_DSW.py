#第一题
def optimal_cut(length):
    '''计算不同长度香肠最大卖多少钱
       length:香肠长度
       output:买最多的钱'''
    if length  <=0:
        return 0
    if optimal_cut_memory[length] == None:
        max_value=0
        for cut in range (length):
            max_value=max(max_value,price_list[cut]+optimal_cut(length-cut-1))
        optimal_cut_memory[length]=max_value   
    return optimal_cut_memory[length]
price_list=[3,5,8,9,10,17,17,20]
optimal_cut_memory = [None]*(len(price_list) + 1)
result = optimal_cut(len(price_list))
print(result)
#2题
work = 'We can know only that we know nothing. And that is the highest degree of human wisdom.'

def histogram_work_words(work):
    """计算work中各个单词出现的次数，
        work:字符串
        output：各个单词与其出现频率相对应的字典"""

    histogram = dict()
    words = work.split()
    for c in words:
        if c.isalpha():
            c = c.lower()
            if c in histogram:
                histogram[c] += 1
            else:
                histogram[c] = 1
    return histogram
dicts = histogram_work_words(work)
for key in dicts:
    print(key,dicts[key],end=' ')
