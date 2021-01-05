class Solution:
    def largeGroupPositions(self, s: str):
        ans = []
        n = len(s)
        a = 0
        for i in range(1, n):
            if s[i] == s[a]:
                continue
            else:
                leng = i - a
                if leng >= 3:
                    ans.append([a, i-1])
                a = i
        if n-a >= 3:
            ans.append([a,n-1])
        return ans
