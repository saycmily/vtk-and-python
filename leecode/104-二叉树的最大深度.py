# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0

        def func(root, ans):
            if root:
                ans += 1
                a = func(root.left, ans)
                b = func(root.right, ans)
                ans = max(a, b)
            return ans
        return func(root, ans)
