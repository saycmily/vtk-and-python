import bisect
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix_sorted_sums = [0]
        ans, now = 0, 0
        for i in nums:
            now += i
            left = bisect.bisect_left(prefix_sorted_sums, now - upper)
            right = bisect.bisect_right(prefix_sorted_sums, now - lower)
            ans += right - left
            bisect.insort(prefix_sorted_sums, now)
        return ans
