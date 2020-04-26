def generate(self, numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    ans = [[1], [1, 1]]
    if numRows == 2:
        return ans
    for i in range(numRows-2):
        clone = ans[-1]
        num = [1]
        for j in range(1, len(clone)):
            num.append(clone[j]+clone[j-1])
        num.append(1)
        ans.append(num)
    return ans
