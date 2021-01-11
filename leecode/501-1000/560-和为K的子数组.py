class Solution:
    def subarraySum(self, nums, k: int) -> int:
        s = 0
        res = 0
        mp = {0: 1}
        for i in range(len(nums)):
            s += nums[i]
            res += mp.get(s-k, 0)
            mp[s] = mp.get(s, 0) + 1
        return res
