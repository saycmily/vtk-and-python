class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m != n:
            return False
        yin, jin = dict(), dict()
        for i in range(m):
            if s[i] in yin or t[i] in jin:
                if yin.get(s[i]) != t[i] or jin.get(t[i]) != s[i]:
                    return False
            yin[s[i]] = t[i]
            jin[t[i]] = s[i]
        return True
