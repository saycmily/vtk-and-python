def grayCode(n):
    ans = []
    for i in range(2**n):
        ans.append(i ^ i >> 1)
    return ans
