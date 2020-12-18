class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            a = abs(nums[i]) - 1
            nums[a] = -abs(nums[a])
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
