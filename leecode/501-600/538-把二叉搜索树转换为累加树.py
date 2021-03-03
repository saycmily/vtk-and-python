# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.nums = []
        def func(node):
            if node:
                func(node.left)
                self.nums.append(node.val)
                func(node.right)
        self.n = 0
        def func1(node):
            if node:
                func1(node.left)
                node.val = sum(self.nums[self.n:])
                self.n += 1
                func1(node.right)
        func(root)
        func1(root)
        return root
