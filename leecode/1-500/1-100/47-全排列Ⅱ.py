def permuteUnique(self, nums):
    def backtrack(first=0):
        if first == n and nums[:] not in res:
            res.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    res = []
    n = len(nums)
    backtrack()
    return res
