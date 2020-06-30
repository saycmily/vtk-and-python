class Solution:
    def findMin(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
