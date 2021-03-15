class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        count = 0
        miss = 1
        idx = 0
        while miss <= n:
            if idx < len(nums) and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                count += 1
                miss += miss
        return count
