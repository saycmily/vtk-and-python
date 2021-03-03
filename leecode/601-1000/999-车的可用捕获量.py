def numRookCaptures(board):
    m = len(board)
    n = len(board[0])
    ans = 0
    for i in range(m):
        if "R" in board[i]:
            x = i
            for j in range(n):
                if board[i][j] == "R":
                    y = j
                    break
            break
    for i in range(x-1, -1, -1):
        if board[i][y] == "B":
            break
        elif board[i][y] == "p":
            ans += 1
            break
    for i in range(y+1, n):
        if board[x][i] == "B":
            break
        elif board[x][i] == "p":
            ans += 1
            break
    for i in range(y-1, -1, -1):
        if board[x][i] == "B":
            break
        elif board[x][i] == "p":
            ans += 1
            break
    for i in range(x+1, m):
        if board[i][y] == "B":
            break
        elif board[i][y] == "p":
            ans += 1
            break
    return ans
