class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            if num % 4:
                return False
            num = num // 4
        return num == 1
