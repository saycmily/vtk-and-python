# Definition for singly-linked list.
import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.listnode = head
        self.n = 0
        while head:
            self.n += 1
            head = head.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        x = random.randint(0, self.n-1)
        clone = self.listnode
        while x:
            clone = clone.next
            x -= 1
        return clone.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()