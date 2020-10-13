# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.li = []
        self.ans = float("inf")
        def func(node):
            if node:
                func(node.left)
                if self.li:
                    x = abs(node.val - self.li[-1])
                    self.ans = min(self.ans, x)
                self.li.append(node.val)
                func(node.right)
        func(root)
        return self.ans
