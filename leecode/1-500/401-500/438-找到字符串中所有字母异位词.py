class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        n = len(p)
        c = Counter(p)
        ans = []
        for i in range(len(s)-n+1):
            if Counter(s[i:i+n]) == c:
                ans.append(i)
        return ans
