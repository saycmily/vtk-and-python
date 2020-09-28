# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        import collections
        if not root:
            return 0
        q = collections.deque([root])
        res = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                res += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
