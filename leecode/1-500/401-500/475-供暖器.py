class Solution:
    def findRadius(self, houses, heaters) -> int:
        houses.sort()
        heaters.sort()
        m = len(houses)
        n = len(heaters)
        res = 0
        cur_heater = 0
        for house in houses:
            while cur_heater < n and heaters[cur_heater] < house:
                cur_heater += 1
            if cur_heater == 0:
                res = max(res, heaters[cur_heater] - house)
            elif cur_heater == n:
                return max(res, houses[-1] - heaters[-1])
            else:
                res = max(res, min(heaters[cur_heater]- house, house - heaters[cur_heater-1]))
        return res
