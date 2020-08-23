
element = input('please input the number for the list:')
shift = input('please input shift steps:')
shift = int(shift)
test_list = list(element)
result_list = []
for i in test_list:
    result_list.append(int(i))

n = len(result_list)
result_list_copy = result_list.copy()
for s in range(n):
    if s + shift < 0:
        result_list_copy[n + s + shift] = result_list[s]
    if s + shift >= 0:
        result_list_copy[s + shift] = result_list[s]

print(result_list_copy)