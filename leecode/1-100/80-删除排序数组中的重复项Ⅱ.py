def removeDuplicates(self, nums):
    if len(nums) < 3:
        return len(nums)
    i = 2
    for num in nums[2:]:
        if num != nums[i - 2]:
            nums[i] = num
            i += 1
    return i
