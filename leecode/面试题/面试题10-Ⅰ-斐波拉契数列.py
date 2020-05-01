class Solution:
    def fib(self, n: int) -> int:
        num = dict()
        num[0] = 0
        num[1] = 1

        def func(n):
            if n in num:
                return num[n]
            num[n] = int((func(n-1) + func(n-2)) % (1e9+7))
            return num[n]
        return func(n)
