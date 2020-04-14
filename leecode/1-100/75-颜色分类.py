def sortColors(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    start = cur = 0
    end = len(nums) - 1
    while cur <= end:
        if nums[cur] == 0:
            nums[start], nums[cur] = nums[cur], nums[start]
            start += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[end] = nums[end], nums[cur]
            end -= 1
        else:
            cur += 1
