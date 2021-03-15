class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        last_s = ""
        cur_num = 0
        for i in s:
            if i.isdigit():
                cur_num = cur_num*10 + int(i)
            elif i == "[":
                stack.append((last_s, cur_num))
                last_s, cur_num = "", 0
            elif i == "]":
                top = stack.pop()
                last_s = top[0] + last_s * top[1]
            else:
                last_s += i
        return last_s
