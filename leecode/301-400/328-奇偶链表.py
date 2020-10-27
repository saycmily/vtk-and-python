# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        o = head
        p = head.next
        e = p
        # 分别将奇偶筛选出来
        while o.next and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = p
        return head
