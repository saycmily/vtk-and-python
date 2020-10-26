class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for a in sorted(set(s)):
            tmp = s[s.index(a):]
            # 看余下的是否能组成所需的字母
            if len(set(tmp)) == len(set(s)):
                return a + self.removeDuplicateLetters(tmp.replace(a, ""))
        return ""
