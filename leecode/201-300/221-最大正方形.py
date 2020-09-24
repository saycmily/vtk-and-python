class Solution:
    def maximalSquare(self, matrix) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        rows, columns = len(matrix), len(matrix[0])
        maxSide = 0
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide
