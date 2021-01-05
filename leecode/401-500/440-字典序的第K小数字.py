class Solution:
    def getNum(self, n, first, last):
        num = 0 
        while first <= n:
            num += min(n+1, last) - first
            first *= 10
            last *= 10
        return num

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:
            num = self.getNum(n, cur, cur+1)
            if num <= k:
                k -= num
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur
