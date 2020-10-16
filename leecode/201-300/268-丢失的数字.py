class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in nums:
            if ans not in nums:
                return ans
            ans += 1
        return max(nums) + 1
