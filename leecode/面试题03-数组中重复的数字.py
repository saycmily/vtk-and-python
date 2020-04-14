class Solution:
    def findRepeatNumber(self, nums) -> int:
        # from collections import Counter
        # c = Counter(nums)
        # return c.most_common(1)[0][0]
        ans = dict()
        for i in nums:
            if i in ans:
                return i
            ans[i] = 1
