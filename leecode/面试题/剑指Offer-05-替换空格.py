class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(" ", "%20")
        ans = str()
        for i in s:
            if i == ' ':
                ans += "%20"
            else:
                ans += i
        return ans
