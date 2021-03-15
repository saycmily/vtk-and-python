class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        a = m-1
        b = 0
        while a >= 0 and b < n and matrix[a][b] != target:
            if matrix[a][b] < target:
                b += 1
            else:
                a -= 1
        if a == -1 or b == n:
            return False
        return True
