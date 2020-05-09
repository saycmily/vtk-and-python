# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False

        def func(nodea, nodeb):
            if not nodeb:
                return True
            if not nodea:
                return False
            return nodea.val == nodeb.val and \
                func(nodea.left, nodeb.left) and func(nodea.right, nodeb.right)
        return func(A, B) or \
            self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
