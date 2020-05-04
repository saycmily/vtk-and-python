class Solution:
    def printNumbers(self, n: int):
        m = 10 ** n
        ans = []
        for i in range(1, m):
            ans.append(i)
        return ans
