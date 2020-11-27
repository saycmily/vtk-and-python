class Solution:
    def pacificAtlantic(self, matrix: list[list[int]]) -> list[list[int]]:
        def dfs(x, y, pre, visited):
            if x < 0 or y < 0 or x >= m or y >= n or matrix[x][y] < pre or visited[x][y]:
                return
            visited[x][y] += 1
            for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(x+i, y+j, matrix[x][y], visited)
        res = []
        m = len(matrix)
        if m < 1:
            return res
        n = len(matrix[0])
        visitedp = [[0] * n for _ in range(m)]
        visiteda = [[0] * n for _ in range(m)]
        for i in range(m):
            dfs(i, 0, matrix[i][0], visitedp)
            dfs(i, n-1, matrix[i][n-1], visiteda)
        for i in range(n):
            dfs(0, i, matrix[0][i], visitedp)
            dfs(m-1, i, matrix[m-1][i], visiteda)
        for i in range(m):
            for j in range(n):
                if visiteda[i][j] and visitedp[i][j]:
                    res.append([i,j])
        return res
