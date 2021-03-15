import random
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = -1
        n = 0
        cun = dict()
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                n = n + 1
                cun[n] = i
        
        return cun[random.randint(1, n)]

a = Solution([1,2,2,3,3,3,3])
b = a.pick(3)
print(b)