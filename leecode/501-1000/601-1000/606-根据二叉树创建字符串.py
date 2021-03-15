# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def func(node, ans):
            ans += str(node.val)
            if node.left:
                ans += "("
                ans = func(node.left, ans) + ")"
            elif node.right:
                ans += "()"
            if node.right:
                ans += "("
                ans = func(node.right, ans) + ")"
            return ans
        if not t:
            return ""
        ans = ""
        return func(t, ans)
