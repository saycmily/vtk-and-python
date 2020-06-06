class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(1, n):
            res = max(res, abs(nums[i]-nums[i-1]))
        return res
