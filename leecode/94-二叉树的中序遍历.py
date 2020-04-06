# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        ans = []

        def func(root):
            if root:
                func(root.left)
                ans.append(root.val)
                func(root.right)
        func(root)
        return ans
