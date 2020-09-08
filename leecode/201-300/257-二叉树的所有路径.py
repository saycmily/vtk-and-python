# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        res = []

        def func(node, lis):
            lis = lis + "->" + str(node.val)
            clone = lis
            if not node.left and not node.right:
                res.append(lis[2:])
                return
            if node.left:
                func(node.left, lis)
            if node.right:
                func(node.right, clone)
        func(root, '')
        return res
