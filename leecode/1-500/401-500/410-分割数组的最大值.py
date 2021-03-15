class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if len(nums) == m:
            return max(nums)
        lo, hi = max(nums), sum(nums)
        while(lo < hi):
            mid = (lo + hi) // 2
            temp, cnt = 0, 1
            for num in nums:
                temp += num
                if temp > mid:
                    temp = num
                    cnt += 1
            if cnt > m:
                lo = mid + 1
            elif cnt <= m:
                hi = mid
        return lo
