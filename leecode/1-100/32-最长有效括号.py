def longestValidParentheses(self, s: str) -> int:
    maxans = 0
    # 利用python列表当作栈使用
    stack = []
    stack.append(-1)
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                maxans = max(maxans, i - stack[-1])
    return maxans
