class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums.reverse()
        n = len(nums)
        dp = [1] * n
        x = nums[0]*10 + nums[1]
        if 0 <= x <= 25:
            dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2, n):
            x = nums[i-1]*10 + nums[i]
            if nums[i-1] and 0 <= x <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]
