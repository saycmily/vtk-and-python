# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        levels = []
        direction = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
                direction.append((direction[-1]+1) % 2)
            if direction[level]:
                levels[level].append(node.val)
            else:
                levels[level].insert(0, node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        direction.append(1)
        helper(root, 0)
        return levels
