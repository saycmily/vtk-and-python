def letterCombinations(digits):
    data = {}
    data[2] = 'abc'
    data[3] = 'def'
    data[4] = 'ghi'
    data[5] = 'jkl'
    data[6] = 'mno'
    data[7] = 'pqrs'
    data[8] = 'tuv'
    data[9] = 'wxyz'
    if digits == "":
        return []
    ans = ['']
    for item in digits:
        # for pre in ans:
        #     for suf in data[int(item)]:
        #         ans.append(pre + suf)
        ans = [pre+suf for pre in ans for suf in data[int(item)]]
    return ans


print(letterCombinations('23'))
