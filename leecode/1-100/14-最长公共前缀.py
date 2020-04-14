def longestCommonPrefix(self, strs):
    if strs == []:
        return ""
    else:
        s = strs[0]
        ans = 0
        flag = True
        for i in range(1, len(s)+1):
            x = s[0:i]
            for item in strs:
                if item[0:i] != x:
                    flag = False
                    break
            if flag:
                ans = i
            else:
                break
        return s[0:ans]
