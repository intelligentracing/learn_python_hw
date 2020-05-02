def nearest(List,target_number,sorted = False):
    if sorted:
        List.sort()
        List[:int(len(List)/2)+1]
