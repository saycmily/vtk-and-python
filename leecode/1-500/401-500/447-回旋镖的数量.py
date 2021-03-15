class Solution:
    def numberOfBoomerangs(self, points) -> int:
        n = len(points)
        if n < 3:
            return 0
        dis = [dict() for i in range(n)]
        for i in range(n):
            a = points[i]
            for j in range(n):
                if j == i:
                    continue
                b = points[j]
                c = a[1] - b[1]
                d = a[0] - b[0]
                e = c*c + d*d
                if e in dis[i]:
                    dis[i][e] += 1
                else:
                    dis[i][e] = 1
        ans = 0
        for i in dis:
            for j in i.values():
                if j > 1:
                    ans = ans + j*(j-1)//2
        return ans*2
