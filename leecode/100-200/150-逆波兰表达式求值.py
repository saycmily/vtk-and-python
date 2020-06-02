class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif s == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif s == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif s == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(s))
        return stack[0]
