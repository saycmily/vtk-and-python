class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] & 1:
                nums[i] = 1
            else:
                nums[i] = 0
        s = 0
        mp = {0: 1}
        res = 0
        for i in range(n):
            s += nums[i]
            res += mp.get(s-k, 0)
            mp[s] = mp.get(s, 0) + 1
            print(mp)
        return res
