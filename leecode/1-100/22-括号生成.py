class Solution:
    def generateParenthesis(self, n):
        # 递归
        # if n == 0:
        #     return [""]
        # elif n == 1:
        #     return ["()"]
        # elif n == 2:
        #     return ["()()", "(())"]
        # result = []
        # for i in range(n):
        #     j = n - 1 - i
        #     temp1 = self.generateParenthesis(i)
        #     temp2 = self.generateParenthesis(j)
        #     result.extend(["(%s)%s" % (p, q) for p in temp1 for q in temp2])
        # return result
        res = []

        def func(ans, l, r):
            if l > n or r > n or r > l:
                return
            if l == n and r == n:
                res.append(ans)
                return
            func(ans+'(', l+1, r)
            func(ans+')', l, r+1)
        ans = ""
        func(ans, 0, 0)
        return res
