class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        n = len(A)
        left = 0
        right = n - 1
        ans = []
        while left <= right:
            if abs(A[left]) < abs(A[right]):
                ans.insert(0, A[right]*A[right])
                right -= 1
            else:
                ans.insert(0, A[left]*A[left])
                left += 1
        return ans
