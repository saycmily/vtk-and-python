# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def func(node):
            if not node:
                return 0
            l = func(node.left)
            r = func(node.right)
            return max(l, r) + 1
        left = func(root.left)
        right = func(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
