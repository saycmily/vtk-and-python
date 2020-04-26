"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, \
    left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if root:
            l, r = root.left, root.right
            while l:
                l.next = r
                l = l.right
                r = r.left
            self.connect(root.left)
            self.connect(root.right)
            return root
        return None
