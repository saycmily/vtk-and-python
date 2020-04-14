# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1.val or not l2.val:
            return l1 if l1.val else l2
        num1 = 0
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
        num2 = 0
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        num = num1 + num2
        ans = ListNode(0)

        while num:
            p = ListNode(num % 10)
            num = num // 10
            tmp = ans.next
            ans.next = p
            p.next = tmp
        return ans.next
