class Solution:
    def isHappy(self, n: int) -> bool:
        cf = []
        while n not in cf:
            cf.append(n)
            ans = 0
            while n:
                ans += (n%10)*(n%10)
                n = n // 10
            n = ans
        if cf[-1] == 1:
            return True
        return False
