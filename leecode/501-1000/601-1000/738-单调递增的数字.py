class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = list(str(N))
        l = len(s)
        flag = l
        for i in range(l-1, 0, -1):
            if s[i] < s[i-1]:
                flag = i
                s[i-1] = str(int(s[i-1]) - 1)
        for i in range(flag, l):
            s[i] = '9'
        return int(''.join(s))
