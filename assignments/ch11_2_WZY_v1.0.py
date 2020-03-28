historgram={}
text = 'We can know only that we know nothing. And that is the highest degree of human wisdom.' # From War and Peace
t=(text.lower().split(" "))
for c in t:
    if c in historgram:
        historgram[c]+=1
    else:
        historgram[c]=1
print (historgram)