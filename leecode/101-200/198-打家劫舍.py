class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        dp = [0 for _ in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]
