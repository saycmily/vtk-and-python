def generateMatrix(self, n):
    array = [[0 for i in range(n)] for j in range(n)]
    c, j = 1, 0
    while c <= n*n:
        # 从左向右
        for i in range(j, n-j):
            array[j][i] = c
            c += 1
        # 从上往下走
        for i in range(j+1, n-j):
            array[i][n-j-1] = c
            c += 1
        # 从右往左走
        for i in range(n-j-2, j-1, -1):
            array[n-j-1][i] = c
            c += 1
        # 从下往上走
        for i in range(n-j-2, j, -1):
            array[i][j] = c
            c += 1
        j += 1
    return array
