import heapq
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        hp = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        # 最外围围栏入堆
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    # 最小堆，保证最矮的围栏出堆
                    heapq.heappush(hp, (heightMap[i][j], i, j))
                    visited[i][j] = True
        ans = 0
        while hp:
            h, r, c = heapq.heappop(hp)
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # 围栏比内部高，可以灌水
                    if h > heightMap[nr][nc]:
                        ans += h - heightMap[nr][nc]
                    # 忽略当前围栏，在(nr, nc)处新建围栏
                    visited[nr][nc] = True
                    # 新的围栏入堆
                    heapq.heappush(hp, (max(h, heightMap[nr][nc]), nr, nc))
        return ans