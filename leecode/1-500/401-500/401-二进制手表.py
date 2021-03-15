class Solution:
    def readBinaryWatch(self, num: int) -> list[str]:
        res = []
        for i in range(12):
            for j in range(60):
                a = str(bin(i)).count('1')
                b = str(bin(j)).count('1')
                if a + b == num:
                    b = str(j)
                    if j < 10:
                        b = '0' + str(j)
                    res.append(str(i) + ':' + b)
        return res
