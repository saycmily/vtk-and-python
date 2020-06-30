class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        while num != 1:
            clone = num
            if num % 2 == 0:
                num = num // 2
            if num % 3 == 0:
                num = num // 3
            if num % 5 == 0:
                num = num // 5
            if clone == num:
                break
        return True if num == 1 else False


a = Solution()
print(a.isUgly(2))
