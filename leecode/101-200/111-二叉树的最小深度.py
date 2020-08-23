# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root) -> int:
        def func(node):
            if not node:
                return 0
            left = func(node.left)
            r = func(node.right)
            if not left or not r:
                return max(left, r) + 1
            return min(left, r) + 1
        return func(root)
