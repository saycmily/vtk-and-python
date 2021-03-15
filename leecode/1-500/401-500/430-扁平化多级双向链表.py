# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        clone = head
        while clone:
            if clone.child:
                clone1 = clone.next
                child = self.flatten(clone.child)
                clone.next = child
                child.prev = clone
                clone.child = None
                if clone1:
                    while clone.next:
                        clone = clone.next
                    clone.next = clone1
                    clone1.prev = clone
            clone = clone.next

        return head
