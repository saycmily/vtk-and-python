from itertools import groupby
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp=[]
        n = len(s)
        add_len = 0
        delete_len = 0
        res = 0
        if n < 6:
            add_len = 6 - n
        if n > 20:
            delete_len = n - 20
        # 至少等于这个结果
        res += delete_len + add_len
        # 判读是否数字 小写字母 大写字母 对于重复数字需要几次操作(插入或者删除)
        is_digit = False
        is_lower = False
        is_upper = False
        repeat = 0
        for i,j in groupby(s[::-1]):
            if i.isdigit(): is_digit = True
            if i.islower(): is_lower = True
            if i.isupper(): is_upper = True
            temp=len(list(j))
            if temp>=3:
                tmp.append(temp)
        #  要按照出现的次数，对3取余，优先删除靠近3的p倍数的，先删至减少一个连续替换，因为可能连续重复的多，但是要删除的少，因此需要y尽可能的多删掉一些连续
        tmp=sorted(tmp,key=lambda x:x%3)
        for i in range(len(tmp)):
            while delete_len>0:
                if tmp[i]%3==0:
                    tmp[i]-=1
                    delete_len-=1
                    tmp=sorted(tmp,key=lambda x:x%3)
                elif tmp[i]%3==1 and delete_len>=2:
                    tmp[i]-=2
                    delete_len-=2
                    tmp=sorted(tmp,key=lambda x:x%3)
                elif tmp[i]%3==2 and delete_len>=3:
                    tmp[i]-=3
                    delete_len-=3
                    tmp=sorted(tmp,key=lambda x:x%3)
                else:
                    break
        for i in range(len(tmp)):
            repeat += tmp[i]//3
        cond = 3 - (is_digit + is_lower + is_upper)
        # 添加
        if add_len >= cond:
            cond = 0
        else:
            cond -= add_len
        # 插入使重复数字之间
        if add_len >= repeat:
            repeat = 0
        else:
            repeat -= add_len
        res += repeat
        # 将重复数字归0
        if repeat >= cond:
            cond = 0
        else:
            cond -= repeat
        return res + cond
