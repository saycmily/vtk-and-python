# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
        

#     def addNum(self, num: int) -> None:
#         if not self.data:
#             self.data.append(num)
#             return
#         if num <= self.data[0]:
#             self.data.insert(0, num)
#             return
#         if num >= self.data[-1]:
#             self.data.append(num)
#             return
#         for i in range(len(self.data) - 1):
#             if self.data[i] < num <= self.data[i+1]:
#                 self.data.insert(i+1, num)
#                 return
        

#     def findMedian(self) -> float:
#         n = len(self.data)
#         if n == 0:
#             return None
#         x = n // 2
#         if n % 2:
#             return self.data[x]
#         return (self.data[x] + self.data[x-1]) / 2
from heapq import *
class MedianFinder:
    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapify(self.max_h)
        heapify(self.min_h)
        
    def addNum(self, num):
       # 每次都插入到最小堆，然后，将最小堆里面的栈顶元素，
       # 取出来，放到最大堆中去，这样就能保证最小堆的堆，都比最大堆的堆顶大
       # 下面的调整，使得最小最大堆元素相差最多为1，而且永远是 最小堆元素个数大于  等于最大堆元素个数
        heappush(self.min_h,num)
        heappush(self.max_h,-heappop(self.min_h))
        if len(self.min_h) < len(self.max_h):
            heappush(self.min_h,-heappop(self.max_h))
            
    def findMedian(self):
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        return self.min_h[0] if max_len!=min_len else (-self.max_h[0]+self.min_h[0])/2.



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()