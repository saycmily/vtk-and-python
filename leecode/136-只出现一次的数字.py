class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                break
            i += 2
        return nums[i]
