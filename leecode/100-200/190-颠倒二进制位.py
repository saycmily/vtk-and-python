class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
        # x = bin(n)[2:]
        # y = '0'*32 + x
        # z = y[-32:][::-1]
        # return int(z, 2)
