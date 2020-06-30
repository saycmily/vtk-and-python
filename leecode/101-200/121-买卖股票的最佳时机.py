def maxProfit(self, prices):
    minprice = float('INF')
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit
