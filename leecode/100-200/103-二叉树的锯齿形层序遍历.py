# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        # 队列循环
        from collections import deque
        ans = []
        if not root:
            return ans
        q = deque([root])
        direction = True
        while q:
            size = len(q)
            ans.append([])
            direction = not direction
            for i in range(size):
                node = q.popleft()
                ans[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not direction:
                ans[-1].reverse()
            direction = not direction
        return ans

        # 数组递归
        # levels = []
        # if not root:
        #     return levels
        # def helper(node, level):
        #     if len(levels) == level:
        #         levels.append([])
        #     levels[level].append(node.val)
        #     if node.left:
        #         helper(node.left, level + 1)
        #     if node.right:
        #         helper(node.right, level + 1)
        # helper(root, 0)
        # for i in range(len(levels)):
        #     if i % 2 != 0:
        #         levels[i].reverse()
        # return levels
