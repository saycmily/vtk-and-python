class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections, functools
        lookup = collections.defaultdict(list)
        for i in range(len(ring)):
            lookup[ring[i]].append(i)

        @functools.lru_cache(None)
        def dfs(cur, k):
            if k == len(key):
                return 0
            res = float("inf")
            for j in lookup[key[k]]:
                x = abs(cur - j)
                min_x = min(x, len(ring) - x)
                res = min(res, min_x + 1 + dfs(j, k + 1))
            return res

        return dfs(0, 0)

a = Solution()
b = a.findRotateSteps("godding", "gd")
print(b)