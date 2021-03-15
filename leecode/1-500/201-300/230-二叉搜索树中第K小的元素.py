# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.jishu, self.res = 0, 0
        def func(node):
            if node:
                func(node.left)
                self.jishu += 1
                if self.jishu == k:
                    self.res = node.val
                    return
                func(node.right)
        func(root)
        return self.res
