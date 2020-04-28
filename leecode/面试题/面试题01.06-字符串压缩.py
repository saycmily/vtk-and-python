def compressString(self, S):
    length = len(S)
    x = 1
    ans = ''
    num = 1
    for index, value in enumerate(S):
        if not index:
            ans += S[0]
            continue
        if value == S[index-1]:
            num += 1
        else:
            ans += str(num)
            ans += value
            num = 1
            x += 2
    ans += str(num)
    return ans if len(ans) < length else S
