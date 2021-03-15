class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)/2
        ready = dict()
        for i in nums:
            if i in ready:
                ready[i] += 1
            else:
                ready[i] = 1
            if ready[i] > n:
                return i
