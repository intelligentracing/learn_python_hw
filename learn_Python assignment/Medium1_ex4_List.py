#Midium1 ex4_List.py
#Author: Yu Qiuhsuang

element = input('please input the number for the list:')
shift = input('please input shift steps:')
shift = int(shift)
test_list = list(element)
result_list = []
for i in test_list:
    result_list.append(int(i))

n = len(result_list)
shift = shift % n
result_list_copy = result_list.copy()
for s in range(n):
    if s + shift < n:
        result_list_copy[s + shift] = result_list[s]
    if s + shift >= n:
        result_list_copy[s + shift - n] = result_list[s]
print(result_list_copy)