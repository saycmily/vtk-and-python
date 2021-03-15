class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        
        if n % 2:
            a = self.integerReplacement(n-1)
            b = self.integerReplacement(n+1)
            return min(a,b) + 1
        n = n >> 1
        return self.integerReplacement(n) + 1
