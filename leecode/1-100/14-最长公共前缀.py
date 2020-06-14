class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        s = strs[0]
        for i in range(1, len(s)+1):
            x = s[:i]
            for item in strs:
                if item[:i] != x:
                    return s[:i-1]
        return s
