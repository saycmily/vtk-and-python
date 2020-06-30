# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: 
            return None
        p = head
        stack = []
        while p:
            stack.append(p)
            p = p.next
        n = len(stack)
        count = (n - 1) // 2
        p = head
        while count:
            tmp = stack.pop()
            tmp.next = p.next
            p.next = tmp
            p = tmp.next
            count -= 1
        stack.pop().next = None
