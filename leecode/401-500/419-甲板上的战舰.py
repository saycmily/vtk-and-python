class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m = len(board)
        n = len(board[0])
        self.visited = [[1] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and self.visited[i][j]:
                    self.func(i, j, board)
                    ans += 1
        return ans
    def func(self, x, y, board):
        m = len(board)
        n = len(board[0])
        self.visited[x][y] = 0
        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
            i = x + a
            j = y + b
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'X' and self.visited[i][j]:
                self.func(i, j, board)