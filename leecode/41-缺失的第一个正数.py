def firstMissingPositive(nums):
    nums = list(set(nums))
    nums.sort()
    flag = False
    x = 0
    for index, value in enumerate(nums):
        if value == 1:
            flag = True
            x = index
            break

    if flag:
        for i in range(x+1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                return nums[i-1] + 1
        return nums[-1] + 1
    else:
        return 1


print(firstMissingPositive([1, 2]))
