class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(' ')
        dicp, dics = {}, {}
        x = 0
        if len(pattern) != len(strs):
            return False
        for i in pattern:
            if i not in dicp:
                dicp[i] = strs[x]
                x += 1
            else:
                if dicp[i] != strs[x]:
                    print(dicp[i], strs[x])
                    return False
                x += 1
        x = 0
        for i in strs:
            if i not in dics:
                dics[i] = pattern[x]
                x += 1
            else:
                if dics[i] != pattern[x]:
                    print(dics[i], pattern[x])
                    return False
                x += 1
        return True
