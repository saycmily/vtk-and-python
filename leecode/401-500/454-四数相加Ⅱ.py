class Solution:
    def fourSumCount(self, A: list[int], B: list[int], C: list[int], D: list[int]) -> int:
        count = 0
        ab_map = dict()
        
        for i in A:
            for j in B:
                a = i + j
                if a in ab_map:
                    ab_map[a] += 1
                else:
                    ab_map[a] = 1
    
        for i in C:
            for j in D:
                a =  - i - j
                if a in ab_map:
                    count += ab_map[a]
                
        return count