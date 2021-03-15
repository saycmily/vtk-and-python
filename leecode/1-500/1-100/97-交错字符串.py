import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from collections import Counter
        if Counter(s1 + s2) != Counter(s3):
            return False

        @functools.lru_cache
        def restore(s1, s2, s3):
            if s3 == '':
                return True
            r1, r2 = False, False
            if s1 and s3[0] == s1[0]:
                r1 = restore(s1[1:], s2, s3[1:])
            if s2 and s3[0] == s2[0]:
                r2 = restore(s1, s2[1:], s3[1:])
            return r1 or r2
        return restore(s1, s2, s3)
