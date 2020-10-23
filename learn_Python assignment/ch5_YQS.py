import random
#ex1.2

# years_list = []
# years1 = input('第一个年份：')
# years2 = input('第二个年份：')


# #sanity check
# # if int_years2 < int_years1:
# #     print('错误！第二个年份应大于第一个年份，请重新输入')
# try:
#     int_years1 = int(years1)
#     int_years2 = int(years2)
# except:
#     print("Not a valid integer input. Exit!")
# else:
#     for years in range(int_years1,int_years2 + 1):
#         if years % 100 == 0:
#             if years % 400 == 0:
#                 years_list.append(years)
#         elif years % 4 == 0:
#             years_list.append(years)
#     print(years_list)

#ex1.3
# def random_sort():
#     num = range(0,100)
#     nums = random.sample(num, 10)
#     t = sorted(nums)
#     print(t)
#     return
# def random_sort2():
#     num = range(0, 100)
#     nums = random.sample(num, 10)
#     for i in range(len(nums) - 1):
#         for j in range(len(nums)-1 - i):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     print(nums)
#     return

# random_sort2()

# def func_test(L = ['a', 'b'], S = 'ab'):
#     L.append('c')
#     S = S +'c'
#     return L, S
# L, S = func_test()
# print(L, S)
# print(func_test(L, S))


print('Please input the first year:')
first = input()
print('Please input the second year:')
second = input()

second = int(second)
# if  first < second:
#     print('Please input the smaller year first')
try: 
    int_first = int(first)
except:
    print('Please input the smaller year first')
else:
    year_list = []
    for i in range(first +1,second):
        if i %100 == 0:
            if i %400 == 0:              
                year_list.append(i)
        elif i %4 == 0:
            year_list.append(i)
    print(year_list)
