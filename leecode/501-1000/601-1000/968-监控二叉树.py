# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            # 0 表示已装监视器, 1表示已有监视器，不用装，2表示需要来监视
            if not node:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 2 or right == 2:
                self.ans += 1
                return 0
            elif left == 0 or right == 0:
                return 1
            else:
                return 2
        if not root:
            return 0
        if dfs(root) == 2:
            self.ans += 1
        return self.ans
