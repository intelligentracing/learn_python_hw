def cut_list(cut_list,d):
    if d==0:
        return cut_list
    else:
        for i in range(0,d):
            cut_list.pop()
        return cut_list

def optimal_cut(price_list):
    best_price=0
    if len(price_list)==1:
        best_price=price_list[0]
    if price_list==[]:
        best_price=0
    else:
        length=len(price_list)
        for i in range (1,length+1):
            temp_list=cut_list(price_list.copy(),i)
            temp_price=price_list[i-1]+optimal_cut(temp_list)
            if temp_price>best_price:
                best_price=temp_price
    return best_price

price_list=[3,5,8,9,10,17,17,20]
print(optimal_cut(price_list))