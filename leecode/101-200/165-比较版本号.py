class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        len1, len2 = len(v1), len(v2)
        m = abs(len1 - len2)
        if len1 > len2:
            v2 += [0] * m
        elif len1 < len2:
            v1 += [0] * m
        for i in range(len(v1)):
            x = int(v1[i])
            y = int(v2[i])
            if x > y:
                return 1
            elif x < y:
                return -1
        return 0
