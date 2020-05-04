# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        clone = head
        clone2 = head.next
        while clone2:
            if clone2.val == val:
                clone.next = clone2.next
                break
            clone2 = clone2.next
            clone = clone.next
        return head
