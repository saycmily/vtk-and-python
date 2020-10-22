class Solution:
    def partitionLabels(self, S: str) -> list[int]:
        # 遍历字符串 找到和起点相同的最后一个字母 
        # 查看此区间里的字母最后的index是否超出区间 超出则更新区间 直至找到最大的index 
        # 则index - i + 1就是所求区间长度 使用cache来存储每个字母的最后出现位置
        if not S:
            return []
        cache, res = {}, []
        n = len(S)
        for i in range(n):
            cache[S[i]] = i

        i = 0
        while i < n:
            end = cache[S[i]]
            j = i + 1
            while j < end:
                if cache[S[j]] > end:
                    end = cache[S[j]]
                j += 1
            res.append(end - i + 1)
            i = end + 1
        return res
