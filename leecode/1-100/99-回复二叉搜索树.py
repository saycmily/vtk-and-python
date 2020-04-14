# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 首先进行中序遍历
        nums = []

        def mid(root):
            if root:
                mid(root.left)
                nums.append(root.val)
                mid(root.right)

        def mid2(root):
            if root:
                mid2(root.left)
                if root.val == first:
                    root.val = second
                elif root.val == second:
                    root.val = first
                mid2(root.right)
        mid(root)
        flag = True
        first, second = 0, 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if flag:
                    first = i
                    flag = False
                else:
                    second = i + 1
                    break
        if second == 0:
            second = nums[first+1]
        else:
            second = nums[second]
        first = nums[first]
        mid2(root)
