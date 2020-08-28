class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for i in range(len(moves)):
            if moves[i] == 'R':
                x += 1
            elif moves[i] == 'L':
                x -= 1
            elif moves[i] == 'U':
                y += 1
            elif moves[i] == 'D':
                y -= 1
        if not x and not y:
            return True
        return False
