# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        while head:
            clone = head
            head = head.next
            clone.next = ans.next
            ans.next = clone
        return ans.next
