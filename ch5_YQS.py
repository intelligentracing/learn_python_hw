import random
#ex1.2
def output_years():
    years_list = []
    years1 = input('第一个年份：')
    years2 = input('第二个年份：')
    int_years1 = int(years1)
    int_years2 = int(years2)

    if years2 < years1:
        print('错误！第二个年份应大于第一个年份，请重新输入')
        return
    for years in range(int_years1,int_years2+1):
        if years % 100 == 0:
            if years % 400 == 0:
                years_list.append(years)
        elif years % 4 == 0:
            years_list.append(years)
    print(years_list)
    return
output_years()
#ex1.3
def random_sort():
    num = range(0,100)
    nums = random.sample(num, 10)
    t = sorted(nums)
    print(t)
    return
def random_sort2():
    num = range(0, 100)
    nums = random.sample(num, 10)
    for i in range(len(nums) - 1):
        for j in range(len(nums)-1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums)
    return

random_sort2()