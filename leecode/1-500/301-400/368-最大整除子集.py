class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return nums
        if len(nums) == 1:
            return nums
        l = len(nums)
        nums.sort()
        dp = [[i] for i in nums]
        for i in range(1, l):
            for j in range(0, i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + [nums[i]], key=len)
        return max(dp, key=len)