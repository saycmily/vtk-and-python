# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        if not grid:
            return
        nums = set(sum(grid,[]))
        if len(nums) == 1: 
            return Node(nums.pop(),True,None,None,None,None)
        n = len(grid)
        grid1 = [grid[i][:n//2] for i in range(n//2)]
        grid2 = [grid[i][n//2:] for i in range(n//2)]
        grid3 = [grid[i][:n//2] for i in range(n//2,n)]
        grid4 = [grid[i][n//2:] for i in range(n//2,n)]
        return Node(0,False,self.construct(grid1),self.construct(grid2),self.construct(grid3),self.construct(grid4))
