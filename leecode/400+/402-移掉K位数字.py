class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remain = len(num) - k
        stack = []
        for s in num:
            while stack and k and stack[-1] > s:
                k -= 1
                stack.pop()
            stack.append(s)
        ans = ''.join(stack[:remain]).lstrip('0')
        if not ans:
            ans = '0'
        return ans
