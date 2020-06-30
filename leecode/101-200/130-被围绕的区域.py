class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def func(i, j):
            for (j, k) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= j < m and 0 <= k < n and board[j][k] == 'O' and (j, k) not in os:
                    os.add((j, k))
                    func(j, k)
        if not board:
            return
        m = len(board)
        n = len(board[0])
        os = set()
        for i in range(n):
            if board[0][i] == 'O' and (0, i) not in os:
                os.add((0, i))
                func(0, i)
            if board[-1][i] == 'O' and (m-1, i) not in os:
                os.add((m-1, i))
                func(m-1, i)
        for i in range(m):
            if board[i][0] == 'O' and (i, 0) not in os:
                os.add((i, 0))
                func(i, 0)
            if board[i][-1] == 'O' and (i, n-1) not in os:
                os.add((i, n-1))
                func(i, n-1)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i, j) not in os:
                    board[i][j] = 'X'
