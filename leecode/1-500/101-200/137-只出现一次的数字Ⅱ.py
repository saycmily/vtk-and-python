class Solution:
    def singleNumber(self, nums) -> int:
        # from collections import Counter
        # c = Counter(nums)
        # return c.most_common()[-1][0]
        ready = dict()
        for i in nums:
            if i in ready:
                ready[i] += 1
            else:
                ready[i] = 1
            if ready[i] == 3:
                del ready[i]
        return list(ready)[0]
