# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        clone = head
        i = 0
        while clone:
            clone = clone.next
            i += 1
        i = i // 2
        while i > 0:
            head = head.next
            i -= 1
        return head
