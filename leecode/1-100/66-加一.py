def plusOne(self, digits):
    s = ''.join(map(str, digits))
    c = int(s) + 1
    x = list(str(c))
    z = map(int, x)
    return z
