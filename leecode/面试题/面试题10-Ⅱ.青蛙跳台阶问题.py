class Solution:
    def numWays(self, n: int) -> int:
        folg = dict()
        folg[0] = 1
        folg[1] = 1
        folg[2] = 2

        def func(n):
            if n in folg:
                return folg[n]
            folg[n] = int((func(n-1) + func(n-2)) % (1e9+7))
            return folg[n]
        return func(n)
