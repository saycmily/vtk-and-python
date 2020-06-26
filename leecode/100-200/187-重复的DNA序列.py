class Solution:
    def findRepeatedDnaSequences(self, s: str):
        exist, res = dict(), list()
        if len(s) <= 10:
            return res
        for i in range(len(s)-9):
            sub_str = s[i:i+10]
            exist[sub_str] = exist.get(sub_str, 0) + 1
            if exist[sub_str] == 2:
                res.append(sub_str)
        return res
