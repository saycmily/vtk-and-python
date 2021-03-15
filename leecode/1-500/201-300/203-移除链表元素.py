# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        clone = head
        while clone and clone.next:
            if clone.next.val == val:
                clone.next = clone.next.next
            else:
                clone = clone.next
        return head
