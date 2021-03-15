class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # 维护三个变量
        m1, m2, m3 = float("-inf"), float("-inf"), float("-inf")
        for i in nums:
            if i == m1 or i == m2 or i == m3:
                continue
            if i > m1:
                m3 = m2
                m2 = m1
                m1 = i
            elif i > m2:
                m3 = m2
                m2 = i
            elif i > m3:
                m3 = i
        if m3 == float("-inf"):
            return m1
        else:
            return m3         
