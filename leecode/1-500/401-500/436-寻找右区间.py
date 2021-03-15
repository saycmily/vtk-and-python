class Solution:
    def findRightInterval(self, intervals):
        start, end = [], []
        result = [-1]*len(intervals)
        for i in range(len(intervals)):
            start.append([intervals[i][0], i])
            end.append([intervals[i][1], i])
        start.sort()
        end.sort()
        i, j = 0, 0
        while i < len(intervals) and j < len(intervals):
            if start[j][0] >= end[i][0]:
                result[end[i][1]] = start[j][1]
                i += 1
                continue
            j += 1
        return result
