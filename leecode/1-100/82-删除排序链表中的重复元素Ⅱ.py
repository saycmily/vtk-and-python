# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p = ListNode(0)
        p.next = head
        clone2 = p
        clone = head
        while clone and clone.next:
            if clone.val != clone.next.val:
                clone = clone.next
                clone2 = clone2.next
            else:
                while clone.next and clone.val == clone.next.val:
                    clone = clone.next
                clone2.next = clone.next
                clone = clone.next
        return p.next
