class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        stack = []
        stack_num = []
        fuhao = ('(', '+', '-', '*', '/')
        i = 0
        while i < n:
            if s[i] in fuhao:
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                x = 0
                while i < n and s[i].isdigit():
                    x = x*10 + int(s[i])
                    i += 1
                stack_num.append(x)
            else:
                f = stack.pop()
                fuhao, num = [], []
                while f != '(':
                    num.append(stack_num.pop())
                    fuhao.append(f)
                    f = stack.pop()
                num.append(stack_num.pop())
                stack_num.append(self.func(fuhao, num))
                i += 1
        return self.func(stack, stack_num)
    
    def func(self, fuhao, num):
        res = num.pop(0)
        jicun = []
        while fuhao:
            f = fuhao.pop(0)
            a = num.pop(0)
            if f == '*':
                res = res * a
            elif f == '/':
                res = res // a
            elif f == '+':
                if fuhao and fuhao[0] != '+' and fuhao[0] != '-':
                    jicun.extend([res,'+'])
                    res = a
                else:
                    if jicun and jicun[-1] == '-':
                        res = res - a
                    else:
                        res = res + a
            else:
                if fuhao and fuhao[0] != '+' and fuhao[0] != '-':
                    jicun.extend([res,'-'])
                    res = a
                else:
                    if jicun and jicun[-1] == '-':
                        res = res + a
                    else:
                        res = res - a
        if not jicun:
            return res
        ans = 0
        while jicun:
            x = jicun.pop(0)
            if x == '+':
                if jicun:
                    ans += jicun.pop(0)
                else:
                    ans += res
            elif x == '-':
                if jicun:
                    ans -= jicun.pop(0)
                else:
                    ans -= res
            else:
                ans = x
        return ans

sol = Solution()
print(sol.calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024"))