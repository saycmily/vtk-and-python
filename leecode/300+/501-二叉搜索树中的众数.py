# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        from collections import Counter
        self.nums = []
        def mid(node):
            if node:
                mid(node.left)
                self.nums.append(node.val)
                mid(node.right)
        mid(root)
        if not self.nums:
            return None
        c = Counter(self.nums).most_common()

        ma = c[0][1]
        ans = [c[0][0]]
        i = 1
        while i < len(c) and c[i][1] == ma:
            ans.append(c[i][0])
            i += 1
        return ans
