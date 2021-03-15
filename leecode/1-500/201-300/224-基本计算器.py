class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        stack = []
        stack_num = []
        fuhao = ('(', '+', '-')
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
                res = 0
                while f != '(':
                    a = stack_num.pop()
                    if f == '+':
                        res = res + a
                    else:
                        res = res - a
                    f = stack.pop()
                res += stack_num.pop()
                stack_num.append(res)
                i += 1
    
        res = 0
        while stack:
            f = stack.pop()
            a = stack_num.pop()
            if f == '+':
                res = res + a
            else:
                res = res - a
        res += stack_num.pop()
        return res
