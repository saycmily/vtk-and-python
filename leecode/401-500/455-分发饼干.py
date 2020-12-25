class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        ans = 0
        for i in s:
            for j in g:
                if j <= i:
                    g.remove(j)
                    ans += 1
                    break
        return ans
