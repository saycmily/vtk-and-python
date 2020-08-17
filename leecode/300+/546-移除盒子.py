import functools


class Solution:
    def removeBoxes(self, boxes) -> int:
        @functools.lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0
            count = 0
            while (i + count) <= j and boxes[i] == boxes[i + count]:
                count += 1

            i2 = i + count
            res = dp(i2, j, 0) + (k + count) ** 2
            for m in range(i2, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dp(i2, m - 1, 0) + dp(m, j, k + count))
            return res

        return dp(0, len(boxes) - 1, 0)
