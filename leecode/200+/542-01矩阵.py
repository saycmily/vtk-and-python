from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        # 刮痧的起始
        zeroes_pos = \  
            [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        Q = deque(zeroes_pos)
        visited = set(zeroes_pos)
        while Q:
            # 一层一层的刮
            i, j = Q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    # 加入已刮痧
                    visited.add((x, y))
                    # 加入下一层要刮痧的
                    Q.append((x, y))
        return matrix
