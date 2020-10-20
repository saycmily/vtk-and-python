class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        x, y = 0, 0
        sl, tl = len(s), len(t)
        for i in s:
            while x < tl:
                if t[x] == i:
                    x += 1
                    y += 1
                    break
                x += 1
                if x == tl:
                    return False
        if y == sl:
            return True
        else:
            return False
