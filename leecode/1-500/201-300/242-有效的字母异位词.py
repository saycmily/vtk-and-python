class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dic = {}
        for i in t:
            if i in t_dic:
                t_dic[i] += 1
            else:
                t_dic[i] = 1
        for i in s:
            if i in t_dic:
                t_dic[i] -= 1
            else:
                return False
        for i in t_dic.values():
            if i != 0:
                return False
        return True
