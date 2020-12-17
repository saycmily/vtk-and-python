class Solution:
    def findMaximumXOR(self, nums) -> int:
        res = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            # 记录前缀
            s = set()
            for num in nums:
                s.add(num & mask)
            # 假设最大值
            tmp = res | (1 << i)
            for t in s:
                if tmp ^ t in s:
                    res = tmp
                    break
        return res