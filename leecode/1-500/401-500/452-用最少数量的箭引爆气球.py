class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        ans = 1
        axis = points[0][1]
        n = len(points)
        for i in range(1, n):
            if axis < points[i][0]:
                ans += 1
                axis = points[i][1]
        return ans
