class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        left, res = A[0], -1
        for i in range(1, len(A)):
            res = max(res, left+A[i]-i)
            left = max(left, A[i]+i)
        return res
