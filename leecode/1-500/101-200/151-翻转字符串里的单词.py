class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        return ' '.join(reversed(res))
