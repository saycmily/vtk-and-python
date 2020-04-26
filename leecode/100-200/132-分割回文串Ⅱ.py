class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n for i in range(n+1)]
        dp[0] = -1
        for i in range(n):
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i+1] = min(dp[i+1], dp[j]+1)
        return dp[-1]
