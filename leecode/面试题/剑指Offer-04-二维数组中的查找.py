import functools


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        @functools.lru_cache
        def func(x, y):
            right, down = False, False
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                if y < n-1:
                    right = func(x, y+1)
                if x < m-1:
                    down = func(x+1, y)
            return right or down
        return func(0, 0)
