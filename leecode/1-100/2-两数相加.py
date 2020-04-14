# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1, l2):
    # 只有一个0节点的链表
    answer = ListNode(0)
    clone_answer = answer
    # 进位的数字
    carry = 0
    while(l1 or l2):
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        num = carry + x + y
        carry = num // 10
        clone_answer.next = ListNode(num % 10)
        clone_answer = clone_answer.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    if(carry == 1):
        clone_answer.next = ListNode(carry)
    return answer.next
