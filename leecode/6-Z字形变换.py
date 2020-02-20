def convert(self, s, numRows):
    ans = {}
    for i in range(numRows):
        ans[i] = str()
    dir = True
    j = -1

    if numRows == 1 or s == '':
        return s
    else:
        for i in range(len(s)):
            if dir:
                j += 1
            else:
                j -= 1
            ans[j] += s[i]
            if i % (numRows-1) == 0 and i != 0:
                dir = not dir

    answer = str()
    for i in range(numRows):
        answer += ans[i]
    return answer
