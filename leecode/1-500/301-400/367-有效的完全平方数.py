class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sn = 1
        while num > 0:
            num -= sn
            sn += 2
        return num == 0