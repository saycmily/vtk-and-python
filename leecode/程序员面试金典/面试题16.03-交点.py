class Solution:
    def intersection(self, start1, end1, start2, end2):
        # 线代知识
        x1, y1, x2, y2, x3, y3, x4, y4 = *start1, *end1, *start2, *end2

        def det(a, b, c, d):
            return a * d - b * c
        d = det(x1 - x2, x4 - x3, y1 - y2, y4 - y3)
        p = det(x4 - x2, x4 - x3, y4 - y2, y4 - y3)
        q = det(x1 - x2, x4 - x2, y1 - y2, y4 - y2)
        if d != 0:
            lam, eta = p / d, q / d
            if not (0 <= lam <= 1 and 0 <= eta <= 1):
                return []
            return [lam * x1 + (1 - lam) * x2, lam * y1 + (1 - lam) * y2]
        if p != 0 or q != 0:
            return []
        t1, t2 = sorted([start1, end1]), sorted([start2, end2])
        if t1[1] < t2[0] or t2[1] < t1[0]:
            return []  # 同一直线上的线段
        return max(t1[0], t2[0])
