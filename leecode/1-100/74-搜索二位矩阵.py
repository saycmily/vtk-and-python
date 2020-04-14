def searchMatrix(self, matrix, target):
    if not matrix or [] in matrix:
        return False
    m = len(matrix)
    n = len(matrix[0])
    ex = -1
    if matrix[0][0] > target:
        return False
    if m == 1:
        ex = 0
    for i in range(1, m):
        if matrix[i][0] == target:
            return True
        if matrix[i][0] > target:
            ex = i - 1
            break
    if ex == -1:
        ex = m-1
    for j in range(n):
        if matrix[ex][j] == target:
            return True
    return False
