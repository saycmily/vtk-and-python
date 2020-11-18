class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list[list[int]]:
        ans = []
        for i in range(R):
            for j in range(C):
                ans.append([i,j])
        ans.sort(key = lambda x: abs(x[0]-r0) + abs(x[1]-c0))
        return ans
