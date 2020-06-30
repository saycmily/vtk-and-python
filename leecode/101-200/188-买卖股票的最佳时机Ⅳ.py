class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if k < 1:
            return 0
        if k >= len(prices)//2:
            ans = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
        t = [[-float("INF"), 0] for _ in range(k)]
        for p in prices:
            t[0][0] = max(t[0][0], -p)
            t[0][1] = max(t[0][1], t[0][0]+p)
            for i in range(1, k):
                t[i][0] = max(t[i][0], t[i-1][1]-p)
                t[i][1] = max(t[i][1], t[i][0]+p)
        return t[k-1][1]
