# 备忘录 动态规划自顶向下  内存消耗更多
def coinChange1(coins, amount):
    mem = dict()

    def dp(n):
        # 查备忘录
        if n in mem:
            return mem[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            sub = dp(n - coin)
            # if sub != -1:
            #     res = min(res, 1 + sub)
            #
            # res = min(res, 1 + sub)  转化为 sub + 1 <= res
            # 都是整数 再转化为 sub < res
            # sub != -1 转化为 sub >= 0
            if sub >= 0 and sub < res:
                res = sub + 1
        # 记备忘录
        mem[n] = res if res < float('INF') else -1
        return mem[n]
    return dp(amount)


#   动态规划 自底向上
def coinChange2(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    # 每增加一种硬币 则对dp列表进行刷新 更效率
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # 每一个数值，使用可用硬币刷新  更好理解
    # for i in range(1, len(dp)):
    #     for coin in coins:
    #         if i < coin:
    #             continue
    #         dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount+1 else -1


coinChange2([1, 2, 5], 11)
