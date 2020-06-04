class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if i == 0 and nums[0] > nums[1]:
                return 0
            elif i == n-1 and nums[-1] > nums[-2]:
                return n-1
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
