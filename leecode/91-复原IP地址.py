class Solution:
    def restoreIpAddresses(self, s: str):
        def backtrack(s, tmp):
            if len(s) == 0 and len(tmp) == 4:
                res.append('.'.join(tmp))
                return
            if len(tmp) < 4:
                for i in range(min(3, len(s))):
                    p, n = s[:i + 1], s[i + 1:]
                    if p and 0 <= int(p) <= 255 and str(int(p)) == p:
                        backtrack(n, tmp + [p])
        res = []
        backtrack(s, [])
        return res
