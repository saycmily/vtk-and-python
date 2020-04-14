def myPow(self, x, n):
    # return pow(x,n)
    i = n
    if i < 0:
        i = -i
    res = 1
    while i != 0:
        if i % 2 != 0:
            res *= x
        x *= x
        i = i // 2
    return res if n > 0 else 1 / res
