class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 二分递归
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # if n == -1:
        #     return 1 / x
        # half = self.myPow(x, n//2)
        # mod = self.myPow(x, n%2)
        # return half * half * mod

        # 快速幂
        m = abs(n)
        res = float(1)
        while m:
            if m & 1:
                res *= x
            x *= x
            m = m // 2
        if n < 0:
            return 1 / res
        return res
