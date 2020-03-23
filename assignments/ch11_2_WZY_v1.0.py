def cut_list(cut_list,d):
    if d==0:
        return cut_list
    else:
        for i in (0,d):
            cut_list.pop()
        return cut_list

def optimal_cut(price_list):
    if len(price_list)==1:
        return price_list[0]
    if price_list==[]:
        return 0
    best_price=0
    length=len(price_list)
    while length>1:
        temp_list=cut_list(price_list.copy(),length)
        temp_price=price_list[length-1]+optimal_cut(temp_list)
        if temp_price>best_price:
            best_price=temp_price
        length-=1
    return best_price

price_list=[3,5,8,9,10,17,17,20]
print(optimal_cut(price_list))