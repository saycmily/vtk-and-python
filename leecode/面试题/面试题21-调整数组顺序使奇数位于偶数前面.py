class Solution:
    def exchange(self, nums):
        left = 0
        r = len(nums) - 1
        while left < r:
            while nums[left] % 2 and left < r:
                left += 1
            while not nums[r] % 2 and left < r:
                r -= 1
            nums[left], nums[r] = nums[r], nums[left]
            left += 1
            r -= 1
        return nums
