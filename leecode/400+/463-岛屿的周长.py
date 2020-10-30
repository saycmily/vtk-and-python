class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def func(zz, n, ans):
            for i in zz:
                j = 0
                while j < n:
                    a = j
                    while j < n and i[j] == 1:
                        j += 1
                    if a != j:
                        ans += 2
                    else:
                        j += 1
            return ans
        n = len(grid)
        m = len(grid[0])
        ans = func(grid, m, 0)
        zz = zip(*grid)
        return func(zz, n, ans)
