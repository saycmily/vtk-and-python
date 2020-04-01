def numDecodings(self, s: str) -> int:
    num = dict()
    num[-1] = 0
    num[0] = 1
    num[1] = 1
    num[2] = 2

    def count(n):
        if n in num:
            return num[n]
        return count(n-1)+count(n-2)
    res = 1
    i = -1
    for index, value in enumerate(s):
        v = int(value)
        if v > 2:
            length = index - i
            i = index
            if v > 6 and index > 0 and int(s[index-1]) == 2:
                res *= count(length-1)
            else:
                res *= count(length)
        elif v == 0:
            length = index - i
            i = index
            res *= count(length-2)
    if i != len(s)-1:
        res *= count(len(s)-i-1)
    return res
