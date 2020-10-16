class Solution:
    def addDigits(self, num: int) -> int:
        def func(num):
            if num < 10:
                return num
            s = str(num)
            new = 0
            for i in s:
                new += int(i)
            return new
        if num < 10:
            return num
        while num >= 10:
            num = func(num)
        return num
