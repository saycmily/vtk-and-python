class Solution:
    def matrixScore(self, A) -> int:
        m = len(A)
        n = len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 1 - A[i][j]
        ans = 0
        for i in zip(*A):
            n -= 1
            ans += 2 ** n * max(i.count(1),i.count(0))
        return ans
