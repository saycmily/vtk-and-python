class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        # n = len(nums)
        # ans = n + 1
        # for i in range(n):
        #     cur = 0
        #     for j in range(i, n):
        #         cur += nums[j]
        #         if cur >= s:
        #             ans = min(ans, j-i+1)
        #             break
        # return ans if ans != n+1 else 0
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans
