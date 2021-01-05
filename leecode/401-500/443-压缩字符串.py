class Solution:
    def compress(self, chars) -> int:
        chars.append("aa")
        n = len(chars)
        j = 0
        cur = 0
        for i in range(1, n):
            if chars[i] == chars[cur]:
                continue
            else:
                chars[j] = chars[cur]
                j += 1
                if i - cur > 1:
                    x = list(str(i-cur))
                    while x:
                        chars[j] = x.pop(0)
                        j += 1
                cur = i
        return j
