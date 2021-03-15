# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        if not headA or not headB:
            return None
        clonea, cloneb = headA, headB
        while clonea != cloneb:
            clonea = clonea.next if clonea else headB
            cloneb = cloneb.next if cloneb else headA
        return clonea
