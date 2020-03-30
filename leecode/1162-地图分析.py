def maxDistance(self, grid):
    # m = len(grid)
    # n = len(grid[0])
    # ludi = []
    # haiyang = []
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             ludi.append((i,j))
    #         else:
    #             haiyang.append((i,j))
    # if not ludi or not haiyang:
    #     return -1
    # distance = [0 for _ in range(len(haiyang))]
    # min_distance = [float("INF") for _ in range(len(haiyang))]
    # k = 0
    # for i,j in haiyang:
    #     for a,b in ludi:
    #         dis = abs(i-a) + abs(j-b)
    #         distance[k] += dis
    #         min_distance[k] = min(min_distance[k],dis)
    #     k += 1
    # max_distance = max(distance)
    # res = 0
    # for index,value in enumerate(distance):
    #     if value == max_distance:
    #         res = max(res,min_distance[index])
    # return res
    m, n = len(grid), len(grid[0])
    dis = [[float("inf") for j in range(n+2)] for i in range(m+2)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if grid[i-1][j-1]:
                dis[i][j] = 0
            else:
                dis[i][j] = min(dis[i-1][j], dis[i][j-1]) + 1
    res = -1
    for i in range(m, 0, -1):
        for j in range(n, 0, -1):
            if grid[i-1][j-1]:
                dis[i][j] = 0
            else:
                dis[i][j] = min(dis[i+1][j]+1, dis[i][j+1]+1, dis[i][j])
                res = max(dis[i][j], res)
    return res if res != float("inf") else -1
