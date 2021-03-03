class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        for point in points:
            x = point[0]
            y = point[1]
            point.append(x*x + y*y)
        points.sort(key = lambda x: x[2])
        return [[points[x][0], points[x][1]] for x in range(K)]
