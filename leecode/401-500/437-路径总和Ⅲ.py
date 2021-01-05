# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.count(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


    def count(self, root, sum):
        if not root:
            return 0
        return int(root.val == sum) + self.count(root.left, sum-root.val) + self.count(root.right, sum-root.val)