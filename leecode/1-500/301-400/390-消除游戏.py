class Solution:
    def lastRemaining(self, n: int) -> int:
        n = range(1, n+1)
        flag = True
        length = len(n)
        while length != 1:
            # n = n[flag or length&1 ::2]
            if flag or length & 1:
                n = n[1::2]
            else:
                n = n[::2]
            flag = not flag
            length = len(n)
        return n[0]
