class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1] * (N + 1)
        cur = 0
        for i in range(1, N + 1):
            if i <= K:
                cur += dp[i - 1]
            if K >= i - W > 0:
                cur -= dp[i - 1 - W]
            dp[i] = cur / W
        return sum(dp[K:])
