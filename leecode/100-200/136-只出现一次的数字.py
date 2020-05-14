class Solution:
    def singleNumber(self, nums):
        ready = set()
        for i in nums:
            if i in ready:
                ready.remove(i)
            else:
                ready.add(i)
        return ready.pop()
