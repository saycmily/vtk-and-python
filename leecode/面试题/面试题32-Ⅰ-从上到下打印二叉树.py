# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        levels = []
        if not root:
            return levels
        q = [root]
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                levels.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return levels
