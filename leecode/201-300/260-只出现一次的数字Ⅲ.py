class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.append(i)
        return ans
