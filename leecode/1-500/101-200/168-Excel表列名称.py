class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n = n - 1
            res = chr(n % 26 + 65) + res
            n = n // 26
        return res
