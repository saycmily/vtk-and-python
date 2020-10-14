class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A:
            return res
        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)
            res += [k] * minnum
        return res
