class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n or \
             (i//10 + i % 10 + j//10 + j % 10) > k or visited[i][j]:
                return 0
            visited[i][j] = True
            return dfs(i+1, j, visited) + dfs(i, j+1, visited) + 1
        visited = [[False for i in range(n)] for j in range(m)]
        return dfs(0, 0, visited)
