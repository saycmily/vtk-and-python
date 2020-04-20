class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length < 2:
            return 0
        dp = [0 for _ in range(4)]
        dp[0] = prices[0]
        dp[2] = float('-inf')

        # dp[j]：i 表示 [0, i] 区间里，状态为 j 的最大收益
        # j = 1：第 1 次买入一支股票
        # j = 2：第 1 次卖出一支股票
        # j = 3：第 2 次买入一支股票
        # j = 4：第 2 次卖出一支股票
        for i in range(1, length):
            dp[0] = min(dp[0], prices[i])
            dp[1] = max(dp[1], prices[i] - dp[0])
            dp[2] = max(dp[2], dp[1] - prices[i])
            dp[3] = max(dp[3], dp[2] + prices[i])
        return max(0, dp[1], dp[3])

        # p = 0
        # ans = []
        # for i in range(1, length):
        #     if prices[i] <= prices[i-1]:
        #         ans.append(prices[i-1]-prices[p])
        #         print(ans)
        #         p = i
        # if prices[-1] > prices[-2]:
        #     ans.append(prices[-1] - prices[p])
        # ans.sort()
        # if len(ans) == 1:
        #     return ans[-1]
        # return ans[-1] + ans[-2]
