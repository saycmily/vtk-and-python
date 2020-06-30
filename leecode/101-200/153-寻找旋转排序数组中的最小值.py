class Solution:
    def findMin(self, nums) -> int:
        ex = nums[0]
        for i in nums[1:]:
            if i >= ex:
                continue
            else:
                return i
        return nums[0]
