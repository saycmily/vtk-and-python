class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) < 2:
            return 0
        intervals.sort()
        i = 1
        ans = 0
        while i != len(intervals):
            a = intervals[i-1][0]
            b = intervals[i-1][1]
            c = intervals[i][0]
            d = intervals[i][1]
            if b > c:
                ans += 1
                if b > d:
                    del intervals[i-1]
                else:
                    del intervals[i]
            else:
                i += 1
        return ans

a = Solution()
b = a.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
print(b)