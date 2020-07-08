class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int):
        if k == 0:
            return []
        elif shorter == longer:
            return [k*longer]
        ans = []
        for i in range(k+1):
            j = k - i
            x = i * longer + j * shorter
            ans.append(int(x))
        return ans
