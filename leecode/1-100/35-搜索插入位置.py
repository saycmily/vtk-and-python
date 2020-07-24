class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for index, value in enumerate(nums):
            if value >= target:
                return index
        return len(nums)
