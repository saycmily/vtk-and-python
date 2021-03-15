def rotate(self, matrix):
    n = len(matrix[0])
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(n):
        matrix[i].reverse()
