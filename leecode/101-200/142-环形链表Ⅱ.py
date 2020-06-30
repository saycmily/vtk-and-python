# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        while head:
            if head not in s:
                s.add(head)
            else:
                return head
            head = head.next
        return None
