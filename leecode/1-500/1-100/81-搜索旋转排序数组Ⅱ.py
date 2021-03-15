def search(self, nums, target):
    if not nums:
        return False
    if len(nums) == 1:
        return nums[0] == target
    if nums[0] == target:
        return True
    if nums[0] > target:
        i = len(nums) - 1
        while i > 0 and nums[i] >= nums[i-1]:
            if nums[i] == target:
                return True
            i -= 1
        if nums[i] == target:
            return True
    else:
        i = 1
        while i < len(nums) and nums[i] >= nums[i-1]:
            if nums[i] == target:
                return True
            i += 1
    return False
