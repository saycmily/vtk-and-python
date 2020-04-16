# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def func(nums):
            if not nums:
                return None
            x = len(nums)//2
            root = TreeNode(nums[x])
            root.left = func(nums[:x])
            root.right = func(nums[x+1:])
            return root
        return func(nums)
