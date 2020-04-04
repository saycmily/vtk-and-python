def getRow(self, rowIndex):
    if rowIndex == 0:
        return [1]
    pre = [1, 1]
    if rowIndex == 1:
        return pre
    for i in range(rowIndex-1):
        num = [1]
        for j in range(1, len(pre)):
            num.append(pre[j]+pre[j-1])
        num.append(1)
        pre = num[:]
    return pre
    # temp = 1
    # res = []
    # for i in range(rowIndex + 1):
    #     res.append(temp)
    #     temp = (temp * (rowIndex - i)) // (i + 1)
    # return res
