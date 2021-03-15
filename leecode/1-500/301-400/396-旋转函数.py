class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        num = 0
        n = len(A)
        num = sum(A)
        F = sum([i*A[i] for i in range(n)])
        ans = F
        for i in range(1, n):
            F += num - n*A[n-i]
            ans = max(ans, F)
        return ans
