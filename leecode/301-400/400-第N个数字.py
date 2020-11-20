class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        weishu = 1
        shuliang = 9
        num = 0
        while n > weishu*shuliang:
            n -= weishu*shuliang
            weishu += 1
            shuliang *= 10
        a = (n + 1) // weishu
        b = n % weishu - 1
        c = shuliang // 9
        d = c + a - 1
        return str(d)[b]
