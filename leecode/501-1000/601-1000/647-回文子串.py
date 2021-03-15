class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    res += 1
                    continue
                cur = s[i:j+1]
                if cur == cur[::-1]:
                    res += 1
        return res
