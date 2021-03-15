class Solution:
    def minMoves(self, nums) -> int:
        x = min(nums)
        ans = 0
        for i in nums:
            ans += i - x
        return ans
