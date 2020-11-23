class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.index(i) == s.rindex(i):
                return s.index(i)
        return -1
