# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque
class Solution:
    def levelOrder(self, root: 'Node'):
        levels = []
        if not root:
            return levels
        q = deque([root])
        while q:
            levels.append([])
            size = len(q)
            for i in range(size):
                node = q.popleft()
                levels[-1].append(node.val)
                for n in node.children:
                    if n:
                        q.append(n)
        return levels
