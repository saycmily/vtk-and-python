# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        ans = []
        if not root:
            return ans

        def func(root, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            if root.left:
                func(root.left, level+1)
            if root.right:
                func(root.right, level+1)
        func(root, 0)
        return ans[::-1]
