# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float("INF")

        def func(node):
            if not node:
                return 0
            left = max(0, func(node.left))
            right = max(0, func(node.right))
            self.ans = max(self.ans, node.val + left + right)
            return max(left, right) + node.val
        func(root)
        return self.ans
