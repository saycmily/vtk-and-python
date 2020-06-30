# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        x = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:x], postorder[:x])
        root.right = self.buildTree(inorder[x+1:], postorder[x:-1])
        return root
