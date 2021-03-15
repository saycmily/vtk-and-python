def nextPermutation(nums):
    i = len(nums) - 1
    while i >= 0 and nums[i] <= nums[i-1]:
        i -= 1
    i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp

    a = nums[i+1:]
    a.reverse()
    nums[i+1:] = a[:]


print(nextPermutation([5, 1, 1]))
