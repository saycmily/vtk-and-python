# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    m = dict()

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.m:
            return self.m[head]
        new = Node(head.val)
        self.m[head] = new
        new.next = self.copyRandomList(head.next)
        new.random = self.copyRandomList(head.random)
        return new
