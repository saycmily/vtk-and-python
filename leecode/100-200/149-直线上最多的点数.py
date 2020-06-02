class Solution:
    def maxPoints(self, points) -> int:
        # def gcd(x, y):
        #     if y == 0:
        #         return x
        #     else:
        #         return gcd(y, x % y)
        import math
        n = len(points)
        if n < 3:
            return n
        res = 0
        # 遍历每个点
        for i in range(n):
            # 与之重合的点数
            duplicate = 0
            # 保存经过当前点的直线中，包含最多点的直线的点数
            cur_max = 0
            m = dict()
            for j in range(i+1, n):
                # 求出分子分母
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                if not x and not y:
                    duplicate += 1
                    continue
                g = math.gcd(x, y)
                if g:
                    x //= g
                    y //= g
                # math.gcd 返回正数
                # 使计入字典的y为非负数，y为0，x为绝对值
                if y < 0:
                    x, y = -x, -y
                elif y == 0:
                    x = abs(x)
                mom = "{}/{}".format(y, x)
                m[mom] = m.get(mom, 0) + 1
                cur_max = max(cur_max, m[mom])
            # 1 代表当前考虑的点，duplicate 代表和当前的点重复的点
            res = max(res, cur_max + duplicate + 1)
        return res
