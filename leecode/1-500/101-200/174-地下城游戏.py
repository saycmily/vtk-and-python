class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon[0])
        n = len(dungeon)
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                elif i == n-1:
                    dp[i][j] = max(1, dp[i][j+1]-dungeon[i][j])
                elif j == m-1:
                    dp[i][j] = max(1, dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]
