class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        return sorted(sum(matrix, []))[k-1]
