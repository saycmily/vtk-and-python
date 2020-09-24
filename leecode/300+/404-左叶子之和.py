# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        def func(node):
            if not node:
                return 
            if node.left:
                if not node.left.left and not node.left.right:
                    self.res += node.left.val
                func(node.left)
            if node.right:
                func(node.right)
        func(root)
        return self.res
