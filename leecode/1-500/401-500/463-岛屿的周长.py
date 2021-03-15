class Solution:
    def islandPerimeter(self, grid):
        def func(zz, ans):
            for i in zz:
                b = ''.join(map(str, i))
                c = b.split('0')
                for d in c:
                    if d:
                        ans += 2
            return ans
    
        ans = func(grid, 0)
        zz = zip(*grid)
        return func(zz, ans)