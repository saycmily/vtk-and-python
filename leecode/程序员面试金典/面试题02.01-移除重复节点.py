# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = set()
        clone = head
        res.add(clone.val)
        while clone.next:
            if clone.next.val in res:
                clone.next = clone.next.next
            else:
                res.add(clone.next.val)
                clone = clone.next
        return head
