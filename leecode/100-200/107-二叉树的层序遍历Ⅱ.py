# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        from collections import deque
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            size = len(q)
            ans.append([])
            for i in range(size):
                node = q.popleft()
                ans[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans[::-1]
