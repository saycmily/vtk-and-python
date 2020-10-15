# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            return False
        fast, slow = head, head
        # 快慢指针，并且翻转前半部
        while fast and fast.next:
            clone = slow.next
            slow.next = slow.next.next
            clone.next = head
            head = clone
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        
        slow = slow.next
        if not fast:
            head = head.next
        # 从slow和head开始比较
        while slow:
            if slow.val == head.val:
                slow = slow.next
                head = head.next
            else:
                return False
        return True
