# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def func(node):
            if not node:
                return [0, 0]
            left = func(node.left)
            right = func(node.right)
            res1 = max(left[0], left[1]) + max(right[0], right[1])
            res2 = node.val + left[0] + right[0]
            return [res1, res2]
        res = func(root)
        print(res)
        return max(res[0], res[1])
