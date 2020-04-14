def massage(self, nums):
    n = len(nums)
    if n == 0:
        return 0

    dp0, dp1 = 0, nums[0]
    for i in range(1, n):
        tdp0 = max(dp0, dp1)   # 计算 dp[i][0]
        tdp1 = dp0 + nums[i]   # 计算 dp[i][1]
        dp0, dp1 = tdp0, tdp1

    return max(dp0, dp1)
