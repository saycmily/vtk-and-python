# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.flag = False

        def backtrack(num=root.val, node=root):
            if not node.right and not node.left:
                if num == sum:
                    self.flag = True
                return
            if node.left:
                backtrack(num+node.left.val, node.left)
            if node.right:
                backtrack(num+node.right.val, node.right)
        backtrack()
        return self.flag
