class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        if not n or n == 1:
            return n
        nums.sort()
        i = 0
        j = 1
        ans = 0
        while j < n:
            if nums[j] == nums[j-1] + 1:
                j += 1
                continue
            ans = max(ans, j-i)
            i = j
            j += 1
        if nums[-1] == nums[-2] + 1:
            ans = max(ans, n-i)
        return ans