class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        max_can = max(candies)
        res = []
        for c in candies:
            if c + extraCandies >= max_can:
                res.append(True)
            else:
                res.append(False)
        return res
