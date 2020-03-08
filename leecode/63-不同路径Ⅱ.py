def uniquePathsWithObstacles(self, obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1:
        return 0
    obstacleGrid[0][0] = 1
    flag = True
    for i in range(1, m):
        if obstacleGrid[i][0] == 1:
            flag = False
        obstacleGrid[i][0] = 1 if flag else 0
    flag = True
    for j in range(1, n):
        if obstacleGrid[0][j] == 1:
            flag = False
        obstacleGrid[0][j] = 1 if flag else 0

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
            else:
                obstacleGrid[i][j] = 0
    return obstacleGrid[m-1][n-1]
