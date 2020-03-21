def exist(self, board, word):
    m = len(board)
    n = len(board[0])
    l = len(word)
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    mem = [[0] * n for _ in range(m)]

    def get_res(x, y, ind):
        if ind == l:
            return True
        if x < 0 or x > m-1 or y < 0 or y > n-1 or mem[x][y] or board[x][y] != word[ind]:
            return False
        mem[x][y] = 1
        for (i, j) in direction:
            if get_res(x + i, y + j, ind + 1):
                return True
        mem[x][y] = 0  # 若查找失败，则将当前访问状态手动置为0
        return False
    for x in range(m):
        for y in range(n):
            if get_res(x, y, 0):
                return True
    return False
