class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        length = len(gas)
        for ans in range(length):
            had = 0
            flag = True
            for i in range(ans, length):
                had = had + gas[i] - cost[i]
                if had < 0:
                    flag = False
            if not flag:
                continue
            for i in range(ans):
                had = had + gas[i] - cost[i]
                if had < 0:
                    flag = False
            if not flag:
                continue
            else:
                return ans
        return -1
