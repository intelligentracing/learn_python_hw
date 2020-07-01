import random
#generate the random list
def random_sort():
    # num = range(0,100)
    nums = random.sample(range(0,100), 10)
    t = sorted(nums)
    print(t)
    return

#generate the random list and sort it
def random_sort2():
    num = range(0, 100)
    nums = random.sample(num, 10)
    for i in range(len(nums) - 1):
        for j in range(len(nums)-1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # print("unsorted list:", nums)
    #use build in method
    # nums.sort()
    print("sorted list:", nums)
    return

random_sort2()