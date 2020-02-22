# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeNthFromEnd(head, n):
    a = head
    b = head
    # i = 0
    # while a.next:
    #     i += 1
    #     a = a.next
    # i = i - n
    # j = 0
    # while j < i:
    #     b = b.next
    #     j += 1
    # b.next = b.next.next
    # return head
    for i in range(n):
        if a.next:
            a = a.next
        else:
            return head.next

    while a.next:
        a = a.next
        b = b.next
    b.next = b.next.next
    return head
