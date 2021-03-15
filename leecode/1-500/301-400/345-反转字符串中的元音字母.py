class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        yuan = 'aeiouAEIOU'
        l = 0
        n = len(s)
        r = n - 1
        while l < n and r > -1 and l < r:
            while l < n and s[l] not in yuan:
                l += 1
            while r > -1 and s[r] not in yuan:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
