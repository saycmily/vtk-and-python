class Solution:
    def twoSum(self, nums, target):
        a = set(nums)
        for i in nums:
            b = target - i
            if b in a:
                return [i, b]
            else:
                a.discard(i)
