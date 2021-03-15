# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        # 递归数组
        # def helper(node, level):
        #     if len(levels) == level:
        #         levels.append([])
        #     levels[level].append(node.val)
        #     if node.left:
        #         helper(node.left, level + 1)
        #     if node.right:
        #         helper(node.right, level + 1)
        # helper(root, 0)
        # return levels

        # 队列循环
        from collections import deque
        q = deque([root])
        while q:
            levels.append([])
            size = len(q)
            for i in range(size):
                node = q.popleft()
                levels[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return levels
