class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        al = dict()
        for i in arr:
            if i in al:
                al[i] += 1
            else:
                al[i] = 1
        alr = set()
        for v in al.values():
            if v in alr:
                return False
            else:
                alr.add(v)
        return True
