import functools
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        @ functools.lru_cache(None)
        def backtrack(res):
            if res == target:
                return 1
            ans = 0
            for i in range(n):
                val = res + nums[i]
                if val > target:
                    break   
                ans += backtrack(val)
            return ans
    
        return  backtrack(0)