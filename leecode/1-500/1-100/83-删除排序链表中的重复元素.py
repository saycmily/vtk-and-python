# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        clone = head
        clone2 = head
        while clone and clone.next:
            while clone.next and clone.next.val == clone.val:
                clone = clone.next
            clone = clone.next
            clone2.next = clone
            clone2 = clone2.next
        return head
