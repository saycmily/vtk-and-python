# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(self, head):
    if not head or not head.next:
        return head

    clone = head.next
    head.next = self.swapPairs(clone.next)
    clone.next = head
    return clone
