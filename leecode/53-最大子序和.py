def maxSubArray(self, nums):
    res = nums[0]
    sum = 0
    for num in nums:
        if sum > 0:
            sum += num
        else:
            sum = num
        res = max(res, sum)
    return res
