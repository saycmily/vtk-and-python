class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ans = re.search(p, s)  # match
        # if ans and ans.group() == s:
        #     return True
        # else:
        #     return False
        if not p:
            return not s
        first_match = bool(s) and p[0] in (".", s[0])
        if len(p) >= 2 and p[1] == "*":
            if first_match:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            return self.isMatch(s, p[2:])
        return first_match and self.isMatch(s[1:], p[1:])
