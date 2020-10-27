import bisect
from itertools import accumulate


class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix_sorted_sums = [0]

        ans = 0
        for sums in accumulate(nums):
            left = bisect.bisect_left(prefix_sorted_sums, sums - upper)
            right = bisect.bisect_right(prefix_sorted_sums, sums - lower)
            ans += right - left
            bisect.insort(prefix_sorted_sums, sums)
        return ans
