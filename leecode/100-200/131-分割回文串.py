class Solution:
    def partition(self, s: str):
        n = len(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s]]
        ans = []
        for i in range(1, n+1):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]:
                right = self.partition(right)
                for j in right:
                    ans.append([left]+j)
        return ans
