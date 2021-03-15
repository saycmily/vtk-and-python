# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int):
        def func(start, end):
            if start > end:
                return [None]
            ans = []
            for i in range(start, end+1):
                left_trees = func(start, i-1)
                right_trees = func(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        tree = TreeNode(i)
                        tree.left = l
                        tree.right = r
                        print(tree)
                        ans.append(tree)
            return ans
        return func(1, n) if n else []
