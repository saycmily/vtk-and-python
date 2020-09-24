# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def func(node1, node2, node3=None):
            if node1 and node2:
                node3 = TreeNode(node1.val + node2.val)
                node3.left = func(node1.left, node2.left)
                node3.right = func(node1.right, node2.right)
                return node3
            if not node1 and not node2:
                return None
            if node1:
                return node1
            return node2
        return func(t1, t2)
