class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 1 or n == 2 or s == s[::-1]:
            return True
        i, j = 0, n-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        s1 = s[:i] + s[i+1:]
        s2 = s[:j] + s[j+1:]
        return s1 == s1[::-1] or s2 == s2[::-1]
