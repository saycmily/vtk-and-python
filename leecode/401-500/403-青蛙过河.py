class Solution:
    def canCross(self, stones: list[int]) -> bool:
        mp = dict()
        for i in stones:
            mp[i] = set()
        mp[0].add(0)

        for i in stones:
            for k in mp[i]:
                for step in [k-1, k, k+1]:
                    if step > 0 and (i+step) in mp:
                        mp[i+step].add(step)
        return len(mp[stones[-1]]) > 0
