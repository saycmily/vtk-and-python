def climbStairs(self, n):
    if n < 3:
        return n
    num = [0]*n
    num[0] = 1
    num[1] = 2
    for i in range(2, len(num)):
        num[i] = num[i-1] + num[i-2]
    return num[-1]
