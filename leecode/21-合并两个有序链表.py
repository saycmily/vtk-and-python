# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    # if !l1:
    #     return l2
    # if !l2:
    #     return l1
    b = ListNode(0)
    a = b
    while l1 and l2:
        if l1.val <= l2.val:
            a.next = ListNode(l1.val)
            l1 = l1.next
        else:
            a.next = ListNode(l2.val)
            l2 = l2.next
        a = a.next
    if l1:
        a.next = l1
    if l2:
        a.next = l2
    return b.next
