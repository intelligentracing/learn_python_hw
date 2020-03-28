

def optimal_cut(length):
    if length in memory:
        return memory[length]
    else:
        if length<=0:
            return 0
        max_value = 0
        for cut in range(0, length):
            max_value = max(max_value, price_list[cut] + optimal_cut(length-cut-1))
        return max_value
 
memory = dict()
price_list = [3,5,8,9,10,17,17,20]
run_again = True
while run_again:
    run_again = False
    length2 = int(input("how long is the sausage")
    result = optimal_cut(length2)
    memory[length2] = result
    print(result)
    run_again = bool(input("run again ?"))

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
    
