# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def identical(self, node_a, node_b):  # 判定两棵树是否相同
        if not node_a and not node_b:  # 两个 node 都为空为 True
            return True
        if node_a is None or node_b is None:  # 一方空，一方不空，为False
            return False
        # 否则说明两个 node 都非空，那么如果两个树相等必须满足3个条件，即当前 node 的值相等，且各自左右子树也对应相等
        return node_a.val == node_b.val and \
            self.identical(node_a.left, node_b.left) and \
            self.identical(node_a.right, node_b.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.identical(s, t):  # 若 s 和 t 对应的两棵树相同则返回True
            return True
        # 不然的话就继续探索 s 的左右子树是否和 t 相等
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
