class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        clone = num
        if num % 2 == 0:
            num = num // 2
        if num % 3 == 0:
            num = num // 3
        if num % 5 == 0:
            num = num // 5
        while num != clone and num != 1:
            clone = num
            if num % 2 == 0:
                num = num // 2
            if num % 3 == 0:
                num = num // 3
            if num % 5 == 0:
                num = num // 5
        return True if num == 1 else False
