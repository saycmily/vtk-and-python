class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        n, m = len(name), len(typed)
        i, x, jicun = 0, 0, ''
        while i < n:
            if x < m and name[i] == typed[x]:
                jicun = name[i]
                i += 1
                x += 1
                continue
            while x < m and typed[x] == jicun:
                x += 1
            if x >= m or typed[x] != name[i]:
                # print(typed[x], name[i])
                return False
        while x < m and typed[x] == jicun:
            x += 1
        if x != m:
            return False
        return True
