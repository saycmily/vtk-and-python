class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        dic = [0] * 101
        for n in nums:
            dic[n] += 1
        ans = []
        for i in nums:
            ans.append(sum(dic[0:i]))
        return ans
