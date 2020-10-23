class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1] * n
        jicun = {i:0 for i in primes}

        for i in range(1, n):
            res = []
            for j in primes:
                x = dp[jicun[j]] * j
                res.append(x)
            dp[i] = min(res)
            for k in range(len(res)):
                if res[k] == dp[i]:
                    jicun[primes[k]] += 1
        
        return dp[-1]

cmily = Solution()
a = cmily.nthSuperUglyNumber(12, [2,7,13,19])
print(a)