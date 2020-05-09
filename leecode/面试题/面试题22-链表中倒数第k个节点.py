# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        length = 0
        clone = head
        while clone:
            length += 1
            clone = clone.next
        x = length - k
        while x:
            head = head.next
            x -= 1
        return head
