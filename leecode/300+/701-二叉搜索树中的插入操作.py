# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.exa = TreeNode()
        def func(node):
            if node:
                func(node.left)
                if node.val < val:
                    self.exa = node
                func(node.right)
        func(root)
        if self.exa.val == 0:
            clone = root
            while clone.left:
                clone = clone.left
            clone.left = TreeNode(val)

        if self.exa.right:
            clone = self.exa.right
            while clone.left:
                clone = clone.left
            clone.left = TreeNode(val)
        else:
            self.exa.right = TreeNode(val)
        return root
