class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        pigs = 1
        a = minutesToTest // minutesToDie + 1
        b = a
        while b < buckets:
            b = a * b 
            pigs += 1
        return pigs
