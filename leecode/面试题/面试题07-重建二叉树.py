# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        x = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:x+1], inorder[:x])
        root.right = self.buildTree(preorder[x+1:], inorder[x+1:])
        return root
