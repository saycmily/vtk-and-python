def mySqrt(self, x: int) -> int:
    # i = 1
    # while i*i <= x:
    #     if i*i <= 0:
    #         break
    #     i += 1
    # return i-1
    if x < 2:
        return x
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2
    return int(x1)
