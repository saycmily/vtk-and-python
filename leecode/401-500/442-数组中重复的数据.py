class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            a = abs(nums[i]) - 1
            if nums[a] < 0:
                ans.append(a + 1)
            else:
                nums[a] = -nums[a]
        return ans
