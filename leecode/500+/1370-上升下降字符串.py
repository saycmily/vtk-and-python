class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        tj = dict()
        for i in s:
            if i in tj:
                tj[i] += 1
            else:
                tj[i] = 1
        tj = sorted(tj.items())
        tj = list(map(list,tj))
        ans = ""
        flag = True
        while n > 0:
            res = ""
            for i in tj:
                if i[1]:
                    res += i[0]
                    i[1] -= 1
                    n -= 1
            if flag:
                ans += res
                flag = False
            else:
                ans = ans + res[::-1]
                flag = True
        return ans