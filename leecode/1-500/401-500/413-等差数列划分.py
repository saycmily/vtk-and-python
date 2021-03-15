class Solution:
    def numberOfArithmeticSlices(self, A: list[int]) -> int:
        i = 2
        n = len(A)
        cur = 2
        ans = 0
        while i < n:
            if A[i] + A[i-2] == 2*A[i-1]:
                cur += 1
            else:
                ans += (cur-1) * (cur-2) // 2
                cur = 2
            i += 1
        ans += (cur-1) * (cur-2) // 2
        return ans
