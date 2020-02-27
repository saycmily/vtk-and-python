def isValidSudoku(self, board):
    row = [set() for _ in range(9)]  # 行剩余可用数字
    col = [set() for _ in range(9)]  # 列剩余可用数字
    block = [set() for _ in range(9)]  # 块剩余可用数字

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                val = int(board[i][j])
                if val in row[i] or val in col[j] or val in block[(i // 3)*3 + j // 3]:
                    return False
                else:
                    row[i].add(val)
                    col[j].add(val)
                    block[(i // 3)*3 + j // 3].add(val)
    return True
