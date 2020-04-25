# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = []

        def add(x, y):
            return x*10 + y

        def func(node, num):
            num.append(node.val)
            if node.left:
                func(node.left, num[:])
            if node.right:
                func(node.right, num[:])
            if not node.left and not node.right:
                ans.append(reduce(add, num))
        func(root, [])
        print(ans)
        return reduce(lambda x, y: x+y, ans)
