class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        res = []
        while i < n:
            start = nums[i]
            while i+1<n and nums[i]+1 == nums[i+1]:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(nums[i]))
            else:
                res.append(str(start) + '->' + str(end))
            i += 1
        return res
