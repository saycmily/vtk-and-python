# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        while head:
            clone = res
            while clone.next and clone.next.val < head.val:
                clone = clone.next
            h = head
            head = head.next
            h.next = clone.next
            clone.next = h
        return res.next
