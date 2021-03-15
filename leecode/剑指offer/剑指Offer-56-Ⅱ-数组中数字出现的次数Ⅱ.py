class Solution:
    def singleNumber(self, nums):
        a = set(nums)
        b = set()
        for i in nums:
            if i in b:
                a.discard(i)
            else:
                b.add(i)
        return a.pop()
