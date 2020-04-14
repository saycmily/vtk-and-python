def lastRemaining(self, n: int, m: int) -> int:
    # ans = 0
    # for i in range(2,n+1):
    #     ans = (ans+m) % i;
    # return ans
    num = [_ for _ in range(n)]
    index = 0
    while n > 1:
        index = (index + m - 1) % n
        del num[index]
        n -= 1
    return num[0]
