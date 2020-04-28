class Solution:
    def singleNumbers(self, nums):
        ans = set()
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.add(i)
        return list(ans)
