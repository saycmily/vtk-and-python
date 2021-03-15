import heapq
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = []

    def addNum(self, val: int) -> None:
        heapq.heappush(self.min_heap, [val, val])

    def getIntervals(self) -> list[list[int]]:
        merged = []
        while self.min_heap:
            x = heapq.heappop(self.min_heap)
            if not merged or merged[-1][1] + 1 < x[0]:
                merged.append(x)
            else:
                merged[-1][1] = max(merged[-1][1], x[1])
        self.min_heap = merged
        return self.min_heap


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()