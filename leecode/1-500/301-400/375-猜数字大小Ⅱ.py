class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                if i == j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = float("inf")
                    for x in range(i, j+1):
                        dp[i][j] = min(dp[i][j], max(dp[i][x-1], dp[x+1][j]) + x)
        return dp[1][n]