class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        dp = [0]*(n+1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, n+1):
                dp[x] += dp[x-coin]
        return dp[-1] % 1000000007
