class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        def func(x, y):
            if x > 0 and (x-1, y) in land:
                land.remove((x-1, y))
                func(x-1, y)

            if x < m-1 and (x+1, y) in land:
                land.remove((x+1, y))
                func(x+1, y)

            if y > 0 and (x, y-1) in land:
                land.remove((x, y-1))
                func(x, y-1)

            if y < n-1 and (x, y+1) in land:
                land.remove((x, y+1))
                func(x, y+1)
        land = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    land.add((i,j))
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) in land:
                    ans += 1
                    func(i, j)
        return ans
