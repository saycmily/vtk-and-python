def reverse(self, x: int) -> int:
    if x < 0:
        s = str(x)[::-1]
        s = s[:-1]
        if (int(s) < -2**31) or (int(s) > (2**31-1)):
            return 0
        return int('-'+s)
    else:
        s = str(x)[::-1]
        if (int(s) < -2**31) or (int(s) > (2**31-1)):
            return 0
        return int(s)
