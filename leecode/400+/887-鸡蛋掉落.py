class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp公式 dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
        dp = [0 for _ in range(K+1)]
        m = 0
        while dp[K] < N:
            m += 1
            for i in range(K, 0, -1):
                dp[i] = dp[i] + dp[i-1] + 1
        return m
