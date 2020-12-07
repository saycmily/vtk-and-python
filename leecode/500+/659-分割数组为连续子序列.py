import heapq
class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        d = {}
        for num in nums:
            if num - 1 not in d:
                if num not in d:
                    d[num] = []
                heapq.heappush(d[num], 1)
            else:
                if num not in d:
                    d[num] = []
                ele = heapq.heappop(d[num - 1])
                if not d[num - 1]:
                    del d[num - 1]
                heapq.heappush(d[num], ele + 1)
        for v in d.values():
            if v[0] < 3:
                return False
        return True