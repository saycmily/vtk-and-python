# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return []

        def backtrack(num=root.val, node=root, mum=[root.val]):
            if not node.right and not node.left:
                if num == sum:
                    self.ans.append(mum[:])
                return
            if node.left:
                mum.append(node.left.val)
                backtrack(num+node.left.val, node.left, mum)
                mum.pop()
            if node.right:
                mum.append(node.right.val)
                backtrack(num+node.right.val, node.right, mum)
                mum.pop()
        self.ans = []
        backtrack()
        return self.ans
