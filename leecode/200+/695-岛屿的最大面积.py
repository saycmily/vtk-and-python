class Solution:
    def maxAreaOfIsland(self, grid):
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def cha(i, j):
            if i > 0 and grid[i-1][j] == 1:
                self.res += 1
                grid[i-1][j] = 0
                cha(i-1, j)
            if j > 0 and grid[i][j-1] == 1:
                self.res += 1
                grid[i][j-1] = 0
                cha(i, j-1)
            if j < n-1 and grid[i][j+1] == 1:
                self.res += 1
                grid[i][j+1] = 0
                cha(i, j+1)
            if i < m-1 and grid[i+1][j] == 1:
                self.res += 1
                grid[i+1][j] = 0
                cha(i+1, j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.res = 1
                    grid[i][j] = 0
                    cha(i, j)
                    ans = max(ans, self.res)
        return ans
