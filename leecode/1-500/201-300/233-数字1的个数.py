import functools
class Solution:
    @functools.lru_cache(None)
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 9:
            return 1
        s = str(n)
        l = len(s)
        a, b = int(s[0]), int(s[1:])
        if a == 1:
            return self.countDigitOne(10**(l-1) - 1) + b + 1 + self.countDigitOne(b)
        else:
            return a * self.countDigitOne(10**(l-1) - 1) + 10**(l-1) + self.countDigitOne(b)
